from import_export import resources
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportMixin

# Register your models here.
from .models import Client, CriminalBackground, Decision, Referral

class ClientResource(resources.ModelResource):

    class Meta:
        model = Client
        fields = ('first_name', 'middle_initial', 'last_name', 'ssn', 'birth_date', 'gender')

class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(CriminalBackground)
admin.site.register(Decision)
admin.site.register(Referral)







