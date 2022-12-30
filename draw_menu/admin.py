from django.contrib import admin

from draw_menu.models import Menu, MenuItem

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Menu)