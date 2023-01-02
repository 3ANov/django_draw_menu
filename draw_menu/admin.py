from django.contrib import admin

from draw_menu.models import Menu, MenuItem


# Register your models here.
class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem)

