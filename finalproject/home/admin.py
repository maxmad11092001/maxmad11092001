from django.contrib import admin
from .models import customer, recharge, category, product, detail, news

# Register your models here.
admin.site.register(customer)
admin.site.register(recharge)
admin.site.register(category)
admin.site.register(product)
admin.site.register(detail)
admin.site.register(news)
