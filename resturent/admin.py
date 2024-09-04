from django.contrib import admin
from .models import Resturent, MenuItem, Modifier, Category, Order, Payment
# Register your models here.

admin.site.register(Resturent)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Modifier)
