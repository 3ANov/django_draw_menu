from django.apps import AppConfig


class DrawMenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'draw_menu'

    def ready(self):
        import draw_menu.signals
