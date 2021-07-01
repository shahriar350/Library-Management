from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', include('auth_app.urls')),
    path('book/', include('book_app.urls')),
    path('admin/', admin.site.urls),
]
