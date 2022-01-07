from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "pv_isolated_app/home.html")


def input_data(request):

    return render(request, "pv_isolated_app/input_data.html")

def show_data(request):
    datos_formulario = request.GET.dict()
    print(datos_formulario)
    #datos_dispositivos = num_dispositivos.SetDispositivos()
    #datos_dic = datos_dispositivos.dispositivos(datos_formulario)
    #print(datos_dic)


    return render(request, "pv_isolated_app/show_data.html", datos_formulario)