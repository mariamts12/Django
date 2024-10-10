from django.http import HttpResponse, JsonResponse

from .models import Product, Category


def store_home_page(request):
    return HttpResponse("Welcome to the Store Home Page!")


def store_categories(request):
    categories = Category.get_all()
    return JsonResponse(categories, safe=False)


def store_products(request):
    products = Product.get_all()
    return JsonResponse(products, safe=False)
