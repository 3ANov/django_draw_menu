from django.db import models

# Create your models here.


class Menu(models.Model):
    """
    Модель для хранения меню
    """
    menu_name = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    """
    Модель для хранения пункта меню
    """
    menu_id = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name='Меню')
    menu_item_text = models.CharField(max_length=100, blank=False, verbose_name='Название пунтка меню')
    link = models.URLField(blank=True)
    parent_menu_item = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='children_menu_item', verbose_name='Родительский подпункт меню')

    def __str__(self):
        return self.menu_item_text



