from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
##pip install requests
def welcome(request):
    return render(request,"home.html")

def about(request):
    return HttpResponse ("<h1 style ='color:green;'> About first page </h1>")

def index(request):
    str="I am Rajesh Kumar Pattnaik"
    data = ["red","green","yellow"]
    context = {"colors" : data , "string":str}
    return render(request,"index.html", context)

def countries(request):
    data = requests.get("https://restcountries.eu/rest/v2/all").json()
    print(data)
    return render(request,"all_countries.html", {"contxt":data})