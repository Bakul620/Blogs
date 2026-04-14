from django.contrib import admin
from .models import Blog, Categories

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ('Title',)}
    list_display = ('Title', 'Author', 'Category', 'Status', 'Is_featured', 'Created_at')
    search_fields = ('id', 'Title', 'Status', 'Category__Category_name')
    list_editable = ('Is_featured',)


admin.site.register(Categories)
admin.site.register(Blog, BlogAdmin)