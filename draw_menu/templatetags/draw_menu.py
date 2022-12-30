from django import template

from draw_menu.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    Menu.objects.get(menu_name=menu_name)
    return