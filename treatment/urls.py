from django.urls import include, path, re_path
from rest_framework import routers

from . import views

app_name = 'treatment'

router = routers.DefaultRouter()
router.register(r'objectives', views.ObjectivesViewSet, basename='objectives')
router.register(r'goals', views.ProbGoalsViewSet)

urlpatterns = [
path('list/', views.treatment_list, name='list'),
path('create/<int:id>/client', views.treatment_create, name='create'),
path('<int:pk>/update', views.treatment_update, name='update'),
path('<int:pk>/note', views.treatment_note, name='note'),

path('objectives/client/<int:pk>', views.ClientObjectivesList.as_view({'get': 'list'}), name='client_objectives'),
path('objectives/list', views.objectives_list, name='objectives_list'),
path('objectives/client/<int:id>/create', views.objective_create, name='objectives_create'),
path('objectives/<int:pk>/update', views.objective_update, name='objectives_update'),
path('objectives/<int:pk>/note', views.objective_note, name='objectives_note'),

path('objectives/<int:pk>/goal/create', views.goal_create, name='goal_create'),
path('objectives/goal/<int:pk>/update', views.goal_update, name='goal_update'),
]
