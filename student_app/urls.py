from django.urls import path, include
from . import views

app_name = 'student'

urlpatterns = [
    path('create/', views.new_student, name='create'),
    path('borrow/', views.borrow_book, name='borrow')
]
