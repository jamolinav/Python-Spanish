from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    #return HttpResponse("vamos bien!")
    return redirect("/time_display")

def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
    }
    return render(request, "index.html", context)

def some_function(request):
    if request.method == "GET":
    	print(request.GET)
    if request.method == "POST":
        print(request.POST)
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
    return redirect("/time_display")
