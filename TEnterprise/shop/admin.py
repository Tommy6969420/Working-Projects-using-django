from django.contrib import admin
from. models import Product,FlashSale,HeroItem,Tags
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','category','subcategory','price','pub_date']
    search_fields = ['product_name','category','subcategory']
    list_filter = ['category','subcategory']
admin.site.register(Product,ProductAdmin)
admin.site.register(FlashSale)
admin.site.register(HeroItem)
admin.site.register(Tags)