from django.urls import path, include
from . import views

app_name = 'book'

urlpatterns = [
    path('new/', views.new_book, name='create'),
    path('all/', views.all_books, name='all'),
    path('author/', views.author_all, name='author'),
    path('category/', views.category, name='category'),

]
