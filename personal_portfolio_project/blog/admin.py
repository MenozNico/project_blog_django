from django.contrib import admin
from django.contrib.admin import register

from . import models

class CategoryPostInline(admin.TabularInline):
    model = models.CategoryPost

@register(models.Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryPostInline
    ]

@register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass






