from django.contrib import admin
from .models import Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display        = ['id', 'nombre', 'activo']
    list_display_links  = ['nombre', 'activo']
    list_filter         = ['nombre']
    search_fields       = ['nombre']
    
admin.site.register(Producto, ProductoAdmin)
