from django.apps import AppConfig


class WeddingappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WeddingApp'
    # def ready(self):
    #     import WeddingApp.signals
