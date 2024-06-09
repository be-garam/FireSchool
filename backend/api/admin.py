from django.contrib import admin

from .models import School, SchoolData

class SchoolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date information', {'fields': ['date_added', 'contents'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'date_added')
    list_filter = ['date_added']
    search_fields = ['name']

admin.site.register(School, SchoolAdmin)
