from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
'''
# Create your views here.
def homeView(request):
    if request.method == 'POST':
        city = request.POST["city"]

        print(city)
        return HttpResponseRedirect(reverse("/"))

'''