from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cases-home'),
    path('client_tabs/', views.client_tabs, name='client-tabs'),
    path('clients/', views.add_client, name='add-client'),
    path('review/', views.review_client, name='review-client'),
    path('assessment/', views.assess_client, name='assess-client'),
    path('referral/', views.refer_client, name='refer-client'),
    path('employer/', views.add_employer, name='add-employer'),
    path('sanction/', views.add_sanction, name='add-sanction'),
    path('courtphase/', views.add_court_phase, name='court-phase'),
    path('courtdate/', views.add_court_date, name='court-date'),
    path('courtfee/', views.add_court_fee, name='court-fee'),
    path('drugscreen/', views.drug_screen, name='drug-screen'),
    path('service/', views.comm_service, name='comm-service'),

]