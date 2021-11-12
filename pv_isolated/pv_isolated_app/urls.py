

from django.urls import path

from pv_isolated_app import views

urlpatterns = [
    path('', views.home, name="HOME"),
    path('calculadora/', views.calculadora, name="CALCULADORA"),
]
