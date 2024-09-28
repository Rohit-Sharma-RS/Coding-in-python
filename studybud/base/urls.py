from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<pk>', views.room, name='room')  # name is very important as we can use url 'name'
    path('create')
    ]