from django.contrib import admin

# Register your models here.
from.models import photo, Category
admin.site.register(Category)
admin.site.register(photo)