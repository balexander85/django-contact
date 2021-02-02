import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Contact, ContactAdmins


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={meta}.csv"
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class ContactAdmin(admin.ModelAdmin, ExportCsvMixin):
    """Admin class for Contact app

    fieldsets are fields displayed on individual contact page
    list_display are the fields displayed on the list of contacts
    """

    actions = ["export_as_csv"]

    fieldsets = [
        ("Contact", {"fields": ["name", "email", "phone", "message"]}),
    ]

    list_display = ("name", "email", "phone", "message", "contact_date")
    list_filter = ["contact_date"]
    readonly_fields = ["message"]
    search_fields = ["name"]


class ContactAdminsAdmin(admin.ModelAdmin):

    list_display = ("email",)


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactAdmins, ContactAdminsAdmin)
