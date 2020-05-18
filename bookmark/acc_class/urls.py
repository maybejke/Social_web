from django.urls import path

from .views import AccLogin

app_name = 'acc_class'

urlpatterns = [
    path('login/', AccLogin.as_view(), name='acc_class_login')
]