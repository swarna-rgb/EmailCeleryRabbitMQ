from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from celery import shared_task
import time
@shared_task
def test_task(duration):
    time.sleep(duration)
    return None

@shared_task
def send_email_task():
    subject = 'Test celery task from Redis'
    message = 'Test celery task, Plz ignore'
    from_email = 'tangodjango01@gmail.com'
    recipient_list = ['starwars121012@gmail.com']
    fail_silently = False
    send_mail(subject, message, from_email, recipient_list,fail_silently)
    return None