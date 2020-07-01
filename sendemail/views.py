from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .tasks import test_task,send_email_task

def test_view(request):
    test_task.delay(10)
    return HttpResponse('<h1>This is test view </h1>')

def send_email_view(request):
    send_email_task.delay()
    return HttpResponse('<h1>Please check your inbox for your order details</h1>')



def test_send_email_task(request):
    subject = 'Test view'
    message = 'Test celery task, Plz ignore'
    from_email = 'tangodjango01@gmail.com'
    recipient_list = ['starwars121012@gmail.com']
    fail_silently = False
    send_mail(subject, message, from_email, recipient_list,fail_silently)
    return HttpResponse('<h1>Sending email..</h1>')
