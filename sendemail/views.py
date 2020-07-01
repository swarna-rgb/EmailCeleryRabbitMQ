from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email_task,test_task
from django.core.mail import send_mail
import time
# Create your views here.
def send_email_view(request):
    sub = 'Celery view Task Check'
    body = 'This is test'
    sender = 'tangodjango01@gmail.com'
    receipients = ['starwars121012@gmail.com', 'test29974@gmail.com', 'swarnapalanisamy1210@gmail.com']
    send_mail(sub, body, sender, receipients)
    return HttpResponse("Sending email")

def test_view(request):
    test_task.delay(10)
    return HttpResponse('<h1>Test view done by celery <h1>')

def async_task(request):
    #test.delay()
    #time.sleep(10)
    send_email_task.delay("Swarna")
    return render(request, 'orderconfirmation.html')
