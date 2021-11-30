from django.contrib import admin
from orders.models import Pizza, Pasta,Topings,Subs,Salads,Dinner
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Pasta)
admin.site.register(Topings)
admin.site.register(Subs)
admin.site.register(Salads)
admin.site.register(Dinner)