'''from django.contrib import admin
from .models import Product

admin.site.register(Product)
# Register your models here.
'''
from django.contrib import admin
from .models import Product, Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'in_stock','category_name')
    search_fields = ('name',)
    list_filter = ('in_stock',)
    ordering = ('-id',)

    def category_name(self, obj):
        return obj.category.name if obj.category else '-'
    category_name.short_description = 'Category'



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)