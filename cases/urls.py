from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cases-home'),
    path('clients/', views.add_client, name='add-client'),
    path('review/', views.review_client, name='review-client'),
    path('assessment/', views.assess_client, name='assess-client'),
    path('referral/', views.refer_client, name='refer-client'),

]