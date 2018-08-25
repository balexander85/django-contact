from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Admin class for Contact app

        fieldsets are
        list_display are
    """
    fieldsets = [
        (
            "Contact",
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
    search_fields = ['name']


admin.site.register(Contact, ContactAdmin)
