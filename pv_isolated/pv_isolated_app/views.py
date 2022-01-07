from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "pv_isolated_app/home.html")


def input_data(request):

    return render(request, "pv_isolated_app/input_data.html")

def show_data(request):
    datos_formulario = request.GET.dict()
    print(datos_formulario)

    return render(request, "pv_isolated_app/show_data.html", datos_formulario)