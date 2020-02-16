from django.contrib import admin

# Register your models here.
from .models import CourtDate,FeeHistory,Phase, PhaseHistory, Screen, Sanction
# 

admin.site.register(CourtDate)
admin.site.register(FeeHistory)
admin.site.register(Phase)
admin.site.register(PhaseHistory)
admin.site.register(Screen)
admin.site.register(Sanction)


