from huey import crontab
from huey.contrib import djhuey
from stockControl.settings import HUEY as huey
from stockControl.models import LoanItem
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, timedelta

# Função para envio de emails
# Recebe um argumento correspondente ao item de empréstimo (ver models.LoanItem)
# O email é enviado para o endereço de email do requerente do empréstimo
# Se o email for enviado com sucesso, a data da última notificação é atualizada
def send_notification_email(item):
    if send_mail(
        "[Estoque-CTI] Seu empréstimo vence em " + str(item.get_days_before_due()) + " dias",
        "Seu empréstimo de " + str(item) + " vence em " + str(item.get_days_before_due()) \
            + " dias. Por favor, devolva-o até " + item.loan.return_date.strftime("%d/%m/%Y") + ".",
        settings.DEFAULT_FROM_EMAIL,
        [item.loan.claimant.email],
        fail_silently=False,
    ) == 1:
        item.loan.last_notification_email = date.today()
        item.loan.save()
        print("Message successfully delivered to " + item.loan.claimant.email)
    else:
        print("Error delivering message to " + item.loan.claimant.email)

# Tarefa de execução periódica
# Executa todos os dias às 8h da manhã, faz três tentativas com 300 segundos (5 minutos) de intervalo cada
@djhuey.db_periodic_task(
    crontab(day="*", hour="*", minute="*"),
    retries=2, retry_delay=300)
@huey.lock_task('db_periodic_task')
def db_periodic_task():

    # Obtém do banco de dados os itens de empréstimo ainda não devolvidos
    # e cujo prazo de devolução é superior à data atual
    due_soon = LoanItem.objects.filter(
        Q(returned=False, loan__return_date__gt=date.today())
    )

    # Filtra os itens para os quais não há nenhuma notificação prévia e
    # cujo prazo de devolução está nos próximos dez dias
    due_in_10_days = due_soon.filter(loan__last_notification_email=None,
                                              loan__return_date__lte=date.today() + timedelta(days=10))

    # Filtra os itens para os quais há uma notificação prévia e
    # cujo último email de notificação foi há pelo menos cinco dias
    due_in_5_days = due_soon.filter(~Q(loan__last_notification_email=None),
                                             loan__last_notification_email__lte=date.today() - timedelta(days=5))

    print("outstanding: " + str(due_soon.count()))
    print("due in 5: " + str(due_in_5_days.count()))
    print("due in 10: " + str(due_in_10_days.count()))

    # Combina os conjuntos obtidos acima e envia emails referentes a cada item
    for item in due_in_5_days.union(due_in_10_days):
        send_notification_email(item)
