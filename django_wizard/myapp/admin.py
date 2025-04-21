'''from django.contrib import admin
from .models import Product

admin.site.register(Product)
# Register your models here.
'''
from django.contrib import admin
from .models import Product, Category, Tag, Profile
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','category_name','tag_list')
    search_fields = ('name',)
    list_filter = ('category',)
    #ordering = ('-id',)

    def category_name(self, obj):
        return obj.category.name if obj.category else '-'
    category_name.short_description = 'Category'

    def tag_list(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    tag_list.short_description = 'Tags'





admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Profile)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)