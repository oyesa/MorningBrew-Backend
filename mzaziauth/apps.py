from django.apps import AppConfig


class MzaziauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mzaziauth'
    
    def ready(self):
        import mzaziauth.signals
