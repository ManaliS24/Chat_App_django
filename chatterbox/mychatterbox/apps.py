from django.apps import AppConfig


class MychatterboxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mychatterbox'

    def ready(self):
        import mychatterbox.signals
