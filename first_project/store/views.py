from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Product, Category


def store_home_page(request):
    return HttpResponse("Welcome to the Store Home Page!")


def store_categories(request):
    categories = Category.objects.filter(parent=None)
    result = {}
    for c in categories:
        subcategories = Category.objects.get_subcategories(c.id)
        products = Product.objects.get_category_products(subcategories)
        result[c] = len(products)
    return render(request, "categories.html", {"categories": result})


def category_products(request, category_id):
    category = Category.objects.get(pk=category_id)
    categories = Category.objects.get_subcategories(category_id)
    products = Product.objects.get_category_products(categories)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    most_expensive = Product.objects.most_expensive_product(products)
    cheapest = Product.objects.cheapest_product(products)
    average = Product.objects.average_price(products)
    total_price = Product.objects.get_total(products)

    context = {
        "category": category,
        "page_obj": page_obj,
        "most_expensive": most_expensive,
        "cheapest": cheapest,
        "average": average,
        "total_category_price": total_price
    }
    return render(request, "category_products.html", context)


def product(request, product_id):
    p = Product.objects.prefetch_related('category').get(pk=product_id)
    return render(request, "product.html", {"product": p})


def store_products(request):
    products = Product.objects.get_all()
    return JsonResponse(products, safe=False)
