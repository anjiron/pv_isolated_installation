

from django.urls import path

from pv_isolated_app import views

urlpatterns = [
    path('', views.home, name="HOME"),
    path('input_data/', views.input_data, name="INPUT_DATA"),
]
