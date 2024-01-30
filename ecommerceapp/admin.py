from django.contrib import admin
from .models import Category, Products
# Register your models here.


#admin.site.register(Category)
#admin.site.register(Products)
class CategoryAdminClass(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdminClass)


class ProductAdminClass(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','stock']
    list_per_page = 20
admin.site.register(Products,ProductAdminClass)