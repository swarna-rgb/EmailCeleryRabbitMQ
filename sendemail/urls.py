from django.urls import path
from . import views
urlpatterns = [
    path('', views.async_task, name='thanks' ),
    path('test/', views.test_view, name='test' ),
    path('email/', views.send_email_view, name='email' ),
]