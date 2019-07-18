from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class IntakeConfig(ModuleMixin, AppConfig):
    name = 'intake'
