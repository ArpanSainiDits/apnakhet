from django.shortcuts import render

# Create your views here.

def desktop(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")

def price(request):
    return render(request, "pricing.html")

def service(request):
    return render(request, "services.html")
