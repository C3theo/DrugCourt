from django.contrib import admin

# Register your models here.
from .models import CriminalBackground,Client,Decision, Referral

# Register your models here.
admin.site.register(Client)
admin.site.register(CriminalBackground)
admin.site.register(Decision)
admin.site.register(Referral)
