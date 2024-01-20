from django.contrib import admin
from .models import *

admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Courses)
admin.site.register(Students)