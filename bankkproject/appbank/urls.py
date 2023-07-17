
from django.contrib import admin
from django.urls import path, include
from appbank import views
urlpatterns = [
    path('',views.home,name='home'),

]