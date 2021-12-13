from django.contrib import admin
from orders.models import *
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Pasta)
admin.site.register(Topings)
admin.site.register(Subs)
admin.site.register(Salads)
admin.site.register(Dinner)
admin.site.register(Ordenes)
admin.site.register(Detallepasta)
admin.site.register(Detallepizza)
admin.site.register(Detalledinner)
admin.site.register(Detallesalads)
admin.site.register(Detallesub)