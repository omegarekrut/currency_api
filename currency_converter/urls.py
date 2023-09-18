from django.urls import path
from . import views

urlpatterns = [
    path('convert_currency/', views.convert_currency, name='convert_currency'),
]