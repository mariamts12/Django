from django.http import HttpResponse


def store_home_page(request):
    return HttpResponse("Welcome to the Store Home Page!")


def store_products(request):
    return HttpResponse("This is the Store Products Page!")


def store_product_detail(request, product_id):
    return HttpResponse(f"Details of product {product_id}")
