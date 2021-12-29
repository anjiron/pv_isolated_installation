from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "pv_isolated_app/home.html")


def input_data(request):

    return render(request, "pv_isolated_app/input_data.html")

def show_data(request):
    #luminarias_req = request.GET['luminarias']
    luminarias_req = {}
    luminarias_req['some_string'] = "sdjfñlaksjdfñalsdkjfañslkdfj"

    return render(request, "pv_isolated_app/show_data.html", luminarias_req)