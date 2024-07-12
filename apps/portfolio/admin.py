from django.contrib import admin
from .models import Personal, About, Experience, Description, Technology, Education, Portfolio, Issuing_Organization


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current',)  # Add a filter for is_current field
    search_fields = ('title', 'company', 'start_date', 'end_date')  # Add search fields
    list_editable = ('is_current',)  # Allow editing is_current directly from the list view
    ordering = ('is_current',)

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'experience', 'order_number')

admin.site.register(Portfolio)
admin.site.register(Personal)
admin.site.register(About)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Description, DescriptionAdmin)
admin.site.register(Technology)
admin.site.register(Education)
admin.site.register(Issuing_Organization)