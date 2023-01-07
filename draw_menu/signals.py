from django.db.models.signals import post_save
from django.dispatch import receiver

from draw_menu.items_cache import cache_item
from draw_menu.models import MenuItem, Menu


@receiver(post_save, sender=MenuItem)
def invalidate_cache_change_menu_items(sender, instance, **kwargs):
    cache_item.delete_items(instance.menu_id.menu_name)


@receiver(post_save, sender=Menu)
def invalidate_cache_change_menu(sender, instance, **kwargs):
    cache_item.delete_items(instance.menu_name)