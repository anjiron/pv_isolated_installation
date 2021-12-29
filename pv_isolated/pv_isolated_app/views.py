from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "pv_isolated_app/home.html")


def input_data(request):

    return render(request, "pv_isolated_app/input_data.html")