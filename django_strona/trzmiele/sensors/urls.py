from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('czujnik/<int:pk>', views.sensorPage, name="sensorPage"),
    path('ciekawostki/', views.ciekawostki, name="ciekawostki"),
    path('o_nas/', views.onas, name="o_nas"),
]

