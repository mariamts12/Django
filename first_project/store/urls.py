from django.urls import path

from .views import *


urlpatterns = [
    path("", store_home_page, name="store_home_page"),
    path("products/", store_products, name="store_products"),
    path(
        "categories/", store_categories, name="store_categories"
    ),
]
