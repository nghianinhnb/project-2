from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('user_code', 'full_name', 'is_active')
    list_display_links = ('user_code', 'full_name')
    ordering = ('-created_at',)
    filter_horizontal = ()
    list_filter = ('user_code', 'full_name')
    fieldsets = ()


admin.site.register(User, CustomUserAdmin)
