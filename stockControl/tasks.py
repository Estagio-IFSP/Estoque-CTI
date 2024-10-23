from huey import crontab
from huey.contrib import djhuey
from stockControl.settings import HUEY as huey
from stockControl.models import LoanItem
from django.core.mail import send_mail
from django.conf import settings

@huey.periodic_task(crontab(minute='*'))
def periodic_task():
    print('Scheduled tasks are running')

# Disparar emails para CTI e para requerente
#   - 5 dias úteis antes do vencimento
#   - 10 dias úteis antes do vencimento
# Disparar emails após atraso para a CTI e para requerente

def send_due_soon_email(item):
    send_mail(
        "[Estoque-CTI] Seu empréstimo vence em " + str(item.get_days_before_due()) + " dias",
        "Seu empréstimo de " + str(item) + " vence em " + str(item.get_days_before_due()) \
            + " dias. Por favor, devolva-o até " + item.loan.return_date.strftime("%d/%m/%Y") \
            + " ou solicite a extensão do prazo.",
        settings.DEFAULT_FROM_EMAIL,
        [item.loan.claimant.email],
        fail_silently=False,
    )

@djhuey.db_periodic_task(
    crontab(day="*", hour="*", minute="*"),
    retries=2, retry_delay=10)
@huey.lock_task('db_periodic_task')
def db_periodic_task():

    print('-----------------------------------------------------------------------')

    loan_items = LoanItem.objects.filter(returned=False)

    for item in loan_items:
        if item.due_check():
            print("Due:   " + str(item) + " from " + str(item.loan) + " by " + str(abs(item.get_days_before_due())) + " days")
        elif item.get_days_before_due() == 10:
            print("In 10: " + str(item) + " from " + str(item.loan) + " in " + str(item.get_days_before_due()) + " days")
            send_due_soon_email(item)
        elif item.get_days_before_due() == 5:
            print("In 5:  " + str(item) + " from " + str(item.loan) + " in " + str(item.get_days_before_due()) + " days")
            send_due_soon_email(item)
        else:
            print("OK:    " + str(item) + " from " + str(item.loan))

    print("Unreturned items: " + str(loan_items.count()))
    print('-----------------------------------------------------------------------')
