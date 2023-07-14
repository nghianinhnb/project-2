from django.contrib import admin
from .models import Subject, Registration


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('year', 'semester', 'subject_code', 'subject_name')
    list_display_links = ('subject_code',)
    ordering = ('-year', '-semester')
    filter_horizontal = ()
    list_filter = ('year',)
    fieldsets = ()

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'tuition_coefficient')
    list_display_links = ('user', 'subject')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Registration, RegistrationAdmin)
