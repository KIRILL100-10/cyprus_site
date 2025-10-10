from django.contrib import admin
from .models import Category, Article, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_per_page = 5
    ordering = ('-created_at',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_at', 'updated_at')
    list_display_links = ('id', 'author')
    list_per_page = 5
    ordering = ('-created_at',)
    search_fields = ('text',)
