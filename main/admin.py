from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Event, Emails_body, Guests


class GuestsResourseces(resources.ModelResource):
    class Meta:
        model = Guests


class GuestsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']
    resource_class = GuestsResourseces

admin.site.register(Event)
admin.site.register(Emails_body)
admin.site.register(Guests,GuestsAdmin)