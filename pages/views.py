from django.shortcuts import render

def home(request):
	Company_name = 'Hello, Veha'
	return render(request, "home.html", {"cn":Company_name})

def about(request):
	from pages.name import namer
	return render(request, "about.html", {"name": namer})

def contact(request):
	return render(request, "contact.html", {})



