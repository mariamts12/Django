from django.urls import path

from .views import *

urlpatterns = [
    path("", order_home_page, name="order_home_page"),
    path("history/", order_history, name="order_history"),
    path("<int:order_id>/", order_detail, name="order_detail"),
]
