from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Pizza, Topping, Sub, Extra, Pasta, Salad, DinnerPlatter, UserCart

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        user = request.user
        request.session['cart_num'] = len(
            UserCart.objects.all().filter(user=user))
        return render(request, "orders/index.html")
    return render(request, "orders/index.html")


def pizza(request):
    context = {
        "user": request.user,
        "pizza": Pizza.objects.all(),
        "topping": Topping.objects.all(),
    }
    return render(request, "orders/pizza.html", context)


def sub(request):
    context = {
        "user": request.user,
        "sub": Sub.objects.all(),
        "extra": Extra.objects.all(),
    }
    return render(request, "orders/sub.html", context)


def dinnerplatter(request):
    context = {
        "user": request.user,
        "dinnerPlatter": DinnerPlatter.objects.all(),
    }
    return render(request, "orders/dinnerplatter.html", context)


def others(request):
    context = {
        "user": request.user,
        "pasta": Pasta.objects.all(),
        "salad": Salad.objects.all(),
    }
    return render(request, "orders/others.html", context)


@login_required
def cart(request):
    user = request.user
    request.session['cart_num'] = len(
        UserCart.objects.all().filter(user=user))
    context = {
        "items": UserCart.objects.all().filter(user=user)
    }
    return render(request, 'orders/cart.html', context)


@login_required
def additem(request):
    user = request.user
    size = request.POST.get('sub_size', False) or request.POST.get(
        'pizza_size', False) or request.POST.get('dp_size', False)
    name = request.POST.get('sub_name', False) or request.POST.get('pizza_style', False) or request.POST.get(
        'dp_name', False) or request.POST.get('sd_name', False) or request.POST.get('pa_name', False)
    price = request.POST.get('sub_price_hidden', False) or request.POST.get('pizza_price_hidden', False) or request.POST.get(
        'dp_price_hidden', False) or request.POST.get('sd_price_hidden', False) or request.POST.get('pa_price_hidden', False)
    extra = request.POST.getlist(
        'extra_name', False) or request.POST.getlist('topping', False)

    if extra == False:
        entry = UserCart(user=user, order=f"{size} {name}", price=price)
    else:
        entry = UserCart(
            user=user, order=f"{size} {name} with extras: {extra}", price=price)
    entry.save()

    return HttpResponseRedirect(reverse("cart"))
