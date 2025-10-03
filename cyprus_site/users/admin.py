from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'show_photo', 'email', 'date_joined')
    list_display_links = ('id', 'username')
    ordering = ('-date_joined',)
    search_fields = ('username', 'email')

    @admin.display(description='Photo')
    def show_photo(self, user):
        return mark_safe(f'<img src="{user.photo.url}" width=100 />') if user.photo else 'No photo'

