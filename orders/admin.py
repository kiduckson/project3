from django.contrib import admin

from .models import Pizza, Topping, Sub, Extra, Pasta, Salad, DinnerPlatter

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Extra)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
