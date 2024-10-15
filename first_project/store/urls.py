from django.urls import path

from .views import *

urlpatterns = [
    path("", store_home_page, name="store_home_page"),
    path("products/", store_products, name="store_products"),
    path(
        "category/", store_categories, name="store_categories"
    ),
    path(
        "category/<int:category_id>/products/", category_products, name="category_products"
    ),
    path(
        "<int:product_id>/", product, name="product_details"
    ),
]
