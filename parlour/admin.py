from django.contrib import admin
from .models import *
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'created_at']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_at']

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'uploaded_at']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author','created_at','rating']
    
class blogsadmin(admin.ModelAdmin):
    list_display = ['title','created_at']

class faqsection(admin.ModelAdmin):
    list_display = ['title','created_at','author']

    
admin.site.site_header = 'Nova Beauty'
admin.site.site_title = 'Nova Beauty'
  
admin.site.register(Catagory, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(CallbackRequest)
admin.site.register(ReviewAndRating,ReviewAdmin)
admin.site.register(blogcat,blogsadmin)
admin.site.register(faq,faqsection)
