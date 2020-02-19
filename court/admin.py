from django.contrib import admin

# Register your models here.
from .models import CourtDates, FeeHistory, Phase, PhaseHistory, Screens, Sanctions
# 

admin.site.register(CourtDates)
admin.site.register(FeeHistory)
admin.site.register(Phase)
admin.site.register(PhaseHistory)
admin.site.register(Screens)
admin.site.register(Sanctions)
