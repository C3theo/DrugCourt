from django.contrib import admin

# Register your models here.
from .models import Objective, ProbGoal, Rating, TxProgress, TxSession

# Register your models here.
admin.site.register(Objective)
admin.site.register(ProbGoal)
admin.site.register(Rating)
admin.site.register(TxProgress)
admin.site.register(TxSession)