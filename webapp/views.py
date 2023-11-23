from django.shortcuts import render


# Create your views here.

def store(request):
    context={}
    return render(request, 'Main.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)
def register(request):
    context = {}
    return render(request, 'register.html', context)


def checkout(request):
    context = {}
    return render(request, 'Checkout.html', context)
