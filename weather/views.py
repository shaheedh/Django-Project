#This is my views.py

from django.shortcuts import render

def weather (request):
	return render(request, "weather.html", {})


