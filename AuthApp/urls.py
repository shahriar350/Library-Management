from django.urls import path, include
from . import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.my_login, name='login'),
    path('register/', views.my_register, name='register'),
]
