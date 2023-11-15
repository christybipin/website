from django.shortcuts import render
from .models import *
from.models import Department,Admin
from .utils import  cartData

# Create your views here.

def store(request):
    context={}
    return render(request, 'webapp/Main.html', context)


def login(request):
    context = {}
    return render(request, 'webapp/login.html', context)
def register(request):
    context = {}
    return render(request, 'webapp/register.html', context)


def checkout(request):
    context = {}
    return render(request, 'webapp/Checkout.html', context)
