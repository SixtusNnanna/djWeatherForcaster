from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def homeView(request):
    if request.method == 'GET':
        city = request.GET.get("city")
    #prints city on the console 
        print(city)
    return render(request, "index.html")

