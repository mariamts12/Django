from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def order_home_page(request):
    return HttpResponse("Welcome to the Order Home Page!")


def order_history(request):
    return HttpResponse("This is the Order History Page!")


def order_detail(request, order_id):
    return HttpResponse(f"Details of order {order_id}")
