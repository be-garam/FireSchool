from django.contrib import admin

from .models import School, SchoolData, SuggestedSchool, UserReport

class SchoolDataInline(admin.TabularInline):
    model = SchoolData
    extra = 3

class UserReportInline(admin.TabularInline):
    model = UserReport
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

# add SuggestedSchool to admin page
class SuggestedSchoolAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'school_name', 'school_link', 'date_suggested')
    list_filter = ['date_suggested']
    search_fields = ['user_name', 'school_name']

class UserReportAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'date_reported', 'error')
    list_filter = ['date_reported']
    search_fields = ['school_name']

admin.site.register(School, SchoolAdmin)
admin.site.register(SuggestedSchool, SuggestedSchoolAdmin)
admin.site.register(UserReport, UserReportAdmin)
