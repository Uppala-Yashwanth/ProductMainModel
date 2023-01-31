from django.contrib import admin
from FirstApp.models import *

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display= ['Title','Description','price','Size','Quality']

admin.site.register(ProductMainModel,productAdmin)

class colourAdmin(admin.ModelAdmin):
    list_display = ['Colour']


admin.site.register(ProductcolorModel,colourAdmin)

class imagemodelAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(productImageModel,imagemodelAdmin)