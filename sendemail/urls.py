from django.urls import path,include
from .views import test_view,send_email_view,test_send_email_task
urlpatterns = [
    path('test/', test_view, name='test'),
    path('', send_email_view, name='email'),
    path('email/', test_send_email_task, name='emailview')

]
