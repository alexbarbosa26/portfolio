from django.apps import AppConfig

class CadastrosConfig(AppConfig):
    name = 'cadastros'

    def ready(self):
        
        from . import updater
        updater.start()
