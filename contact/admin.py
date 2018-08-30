from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Admin class for Contact app

        fieldsets are fields displayed on individual contact page
        list_display are the fields displayed on the list of contacts
    """
    fieldsets = [
        (
            'Contact',
            {
                'fields': [
                    'name',
                    'email',
                    'phone',
                    'message'
                ]
            }
        ),
    ]

    list_display = (
        'name',
        'email',
        'phone',
        'message',
        'contact_date'
    )
    list_filter = ['contact_date']
    readonly_fields = ['message']
    search_fields = ['name']


admin.site.register(Contact, ContactAdmin)
