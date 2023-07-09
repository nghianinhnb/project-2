from django.contrib import admin

from .models import New

# Register your models here.
class NewAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'title', 'author')
    ordering = ('-created_at',)
    filter_horizontal = ()
    list_filter = ('author',)
    fieldsets = ()


admin.site.register(New, NewAdmin)
