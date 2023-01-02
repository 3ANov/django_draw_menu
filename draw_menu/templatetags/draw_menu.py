from django import template
from django.db.models import Count

from draw_menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('draw_menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.select_related('parent_menu_item').filter(menu_id__menu_name=menu_name,
                                                                            parent_menu_item__isnull=True)

    return {
       'menu_items': menu_items
    }
