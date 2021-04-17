# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	message = "Salut tout le monde !"
	return render(request, "store/home.html", {})
