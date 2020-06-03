from celery.schedules import crontab
from celery.task import periodic_task
from django.core.mail import EmailMessage
from django.conf import settings
from pathlib import Path
import os

path = Path(__file__).parent.absolute()
outfile_path = os.path.join(path, "..", "output.csv")


@periodic_task(run_every=(crontab(minute="*/1")), name="mail-report")
def mail_analysis_report():

    subject = "Mail by rachit"
    message = "Please find the attached file for analysed data"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        "rachitg747@gmail.com",
    ]
    output_file = open(outfile_path).read()
    email = EmailMessage(subject, message, email_from, recipient_list)
    email.attach("analysed_data.csv", output_file, "text/csv")
    email.send(fail_silently=False)
    print("Mail sent")
