from django.contrib import admin
from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('year', 'semester', 'subject_code', 'subject_name')
    list_display_links = ('subject_code',)
    ordering = ('-year', '-semester')
    filter_horizontal = ()
    list_filter = ('subject_code', 'year')
    fieldsets = ()


admin.site.register(Subject, SubjectAdmin)
