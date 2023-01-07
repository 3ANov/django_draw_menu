from django import template

from draw_menu.items_cache import cache_item
from draw_menu.models import MenuItem
from draw_menu.templatetags.templatetags_utils import group_by_menu_items

register = template.Library()


@register.inclusion_tag('draw_menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = cache_item.get_or_set_items(menu_name)
    return {
       'menu_items': group_by_menu_items(menu_items, context['request'].path)
    }
