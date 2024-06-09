from django.contrib import admin

from .models import School, SchoolData

class SchoolDataInline(admin.TabularInline):
    model = SchoolData
    extra = 3

class SchoolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date information', {'fields': ['date_added', 'urls', 'contents'], 'classes': ['collapse']}),
    ]
    inlines = [SchoolDataInline]
    list_display = ('name', 'date_added')
    list_filter = ['date_added']
    search_fields = ['name']

admin.site.register(School, SchoolAdmin)
