from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from store.models import Category
from store.models import Product
from .models import *
# Register your models here.
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','original_price','quantity','created_at')
    search_fields = ['name','original_price','quantity','created_at']
    list_per_page = 2
    
admin.site.register(Product,ProductAdmin)