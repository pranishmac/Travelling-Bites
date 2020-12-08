from django.contrib import admin

# Register your models here.

from .models import item
from .models import order
admin.site.register(item)
admin.site.register(order)