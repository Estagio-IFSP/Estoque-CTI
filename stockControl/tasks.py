from huey import crontab
from huey.contrib import djhuey
from stockControl.settings import HUEY as huey
from stockControl.models import LoanItem
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, timedelta

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

@djhuey.db_periodic_task(
    crontab(day="*", hour="*", minute="*"),
    retries=2, retry_delay=10)
@huey.lock_task('db_periodic_task')
def db_periodic_task():

    print('-----------------------------------------------------------------------')

    total_items = LoanItem.objects.all().count()
    print("Total items: " + str(total_items))

    not_due_yet_items = LoanItem.objects.filter(
        Q(returned=False, loan__return_date__gt=date.today())
    )
    print("Items not due yet: " + str(not_due_yet_items.count()))

    due_in_10_days = not_due_yet_items.filter(loan__last_notification_email=None, loan__return_date__lte=date.today() + timedelta(days=10))
    print("Items due in 10 days: " + str(due_in_10_days.count()))

    due_in_5_days = not_due_yet_items.filter(~Q(loan__last_notification_email=None), loan__last_notification_email__lte=date.today() - timedelta(days=5))
    print("Items due in 5 days: " + str(due_in_5_days.count()))

    for item in due_in_5_days:
        print(" > [for due in 5] Sending email regarding " + str(item) + " from " + str(item.loan) + " due in " + str(abs(item.get_days_before_due())) + " days ")
        send_notification_email(item)

    for item in due_in_10_days:
        print(" > [for due in 10] Sending email regarding " + str(item) + " from " + str(item.loan) + " due in " + str(abs(item.get_days_before_due())) + " days ")
        send_notification_email(item)

    print('-----------------------------------------------------------------------')
