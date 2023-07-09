from django.contrib import admin

from .models import Complaint

# Register your models here.
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('complaint_id', 'sender', 'title', 'created_at', 'updated_at')
    list_display_links = ('complaint_id', 'sender')
    ordering = ('-created_at',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Complaint, ComplaintAdmin)
