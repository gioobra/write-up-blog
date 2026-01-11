from django.contrib import admin
from .models import Post, Category
# Register your models here.

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.site.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}