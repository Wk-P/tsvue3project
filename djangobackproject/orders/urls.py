from django.urls import path
from orders.views import Orders

urlpatterns = [
    path("all", Orders.as_view(), name="orders_list"),
]