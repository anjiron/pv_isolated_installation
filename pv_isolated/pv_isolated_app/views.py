from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "pv_isolated_app/home.html")


def calculadora(request):

    return render(request, "pv_isolated_app/calculadora.html")