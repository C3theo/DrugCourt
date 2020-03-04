"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import routers

from core import views
from treatment.urls import router as tx_router
from intake.urls import router as intake_router

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.registry.extend(tx_router.registry)
router.registry.extend(intake_router.registry)

admin.site.site_header = "Accountibiity Court Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('', RedirectView.as_view(url='/home/')),
    path('home/', include('core.urls', namespace='core')),
    path('intake/', include('intake.urls', namespace='intake')),
    path('notes/', include('scribe.urls', namespace='scribe')),
    path('court/', include('court.urls', namespace='court')),
    path('treatment/', include('treatment.urls', namespace='treatment')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
