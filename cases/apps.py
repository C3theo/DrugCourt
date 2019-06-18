from django.apps import AppConfig

class CaseConfig(AppConfig):
    name = 'cases'

    def ready(self):
        from . import signals

