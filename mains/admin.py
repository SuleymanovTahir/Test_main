from django.contrib import admin
from .models import *

# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Courses)
admin.site.register(Students)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    # list_display='name','created','updated','publish',
    # # readonly_fields=('created','updated',)
    # fieldsets=(('1',{
    #     # 'fields':('created',)
    # }),
    # ('2',{'fields':('publish',)}),
    # ('3',{'fields':('name','updated',)}))
    
@admin.register(Icecream)
class IcecreamAdmin(admin.ModelAdmin):
    list_display=('id','name','price')
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    # raw_id_fields = ['name']
    # date_hierarchy = 'publish'

