from django.contrib import admin

from .models import Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'user', 'title')
    ordering = ('-created_at',)
    list_filter = ()
    fieldsets = ()


admin.site.register(Notification, NotificationAdmin)
