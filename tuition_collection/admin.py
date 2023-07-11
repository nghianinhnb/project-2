from django.contrib import admin

from .models import TuitionCollection

# Register your models here.
class TuitionCollectionAdmin(admin.ModelAdmin):
    list_display = ('year', 'semester', 'school_year', 'credit_fee', 'tuition_collection_start', 'tuition_collection_end')
    list_display_links = ('school_year',)
    ordering = ('-year', '-semester', 'school_year')
    filter_horizontal = ()
    list_filter = ('year', 'school_year')
    fieldsets = ()


admin.site.register(TuitionCollection, TuitionCollectionAdmin)
