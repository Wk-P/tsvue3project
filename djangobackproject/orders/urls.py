from django.urls import path
from orders.views import Orders, OrderCreate

urlpatterns = [
    path("all/", Orders.as_view(), name="orders_list"),
    path("create/", OrderCreate.as_view(), name="orders_list"),
]