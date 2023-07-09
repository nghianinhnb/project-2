from django.contrib import admin

from .models import TuitionDebt

# Register your models here.
class TuitionDebtAdmin(admin.ModelAdmin):
    list_display = ('user', 'ammount')
    list_display_links = ('user',)
    ordering = ()
    filter_horizontal = ()
    list_filter = ('user',)
    fieldsets = ()


admin.site.register(TuitionDebt, TuitionDebtAdmin)
