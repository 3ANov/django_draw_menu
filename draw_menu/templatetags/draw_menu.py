from django import template

from draw_menu.models import MenuItem
from draw_menu.templatetags.templatetags_utils import group_by_menu_items

register = template.Library()


@register.inclusion_tag('draw_menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(menu_id__menu_name=menu_name)

    return {
       'menu_items': group_by_menu_items(list(menu_items.values()), context['request'].path)
    }
