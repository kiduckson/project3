from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("additem/", views.additem, name="additem"),
    path("pizza/", views.pizza, name="pizza"),
    path("sub/", views.sub, name="sub"),
    path("dinnerplatter/", views.dinnerplatter, name="dinnerplatter"),
    path("others/", views.others, name="others"),
    path("orderitem/", views.orderitem, name="orderitem")
]
