from django.urls import path, include
from . import views

app_name = 'book'

urlpatterns = [
    path('new/', views.new_book, name='create'),
    path('category/', views.category, name='category'),

]
