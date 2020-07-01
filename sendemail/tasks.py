from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
import time
from celery import Celery
import time

celery = Celery('AsyncTask',broker='amqp://localhost')

@shared_task
def test_task(duration):
    time.sleep(duration)
    return None

@shared_task
def send_email_task(name):
   # time.sleep(10)
    sub = 'Celery Async Task Check'
    body = 'This is to test celery task {} - plz ignore'.format(name)
    sender = 'tangodjango01@gmail.com'
    #receipient = ['starwars121012@gmail.com']
    #new_receipient = ['test29974@gmail.com']
    new_receipient = ['swarnapalanisamy1210@gmail.com']
    send_mail(sub,body,sender,new_receipient)
    return None

