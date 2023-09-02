from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def burger_list(request):
    return render(request, "burger_list.html")

def pseudo_recomm_research(request):
    return render(request, "index.html")