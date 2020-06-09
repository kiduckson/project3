from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, Topping, Sub, Extra, Pasta, Salad, DinnerPlatter

# Create your views here.


def index(request):
    context = {
        "user": request.user,
        "pizza": Pizza.objects.all(),
        "topping": Topping.objects.all(),
        "sub": Sub.objects.all(),
        "extra": Extra.objects.all(),
        "pasta": Pasta.objects.all(),
        "salad": Salad.objects.all(),
        "dinnerPlatter": DinnerPlatter.objects.all(),
    }

    return render(request, "orders/index.html", context)
