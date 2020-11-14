from django.contrib import admin

# Register your models here.
from app.models import Category, Budget, Purchase


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Budget)
admin.site.register(Purchase)
