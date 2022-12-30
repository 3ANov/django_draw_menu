from django.db import models

# Create your models here.


class MenuItem(models.Model):
    """
    Модель для хранеия пункта меню
    """
    menu_item_text = models.CharField(max_length=100, blank=False, verbose_name='Название пунтка меню')
    link = models.URLField()
    sub_menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE, verbose_name='Подпункт меню', blank=True, null=True)


class Menu(models.Model):
    """
    Модель для хранения меню
    """
    menu_name = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE, verbose_name='Пункт меню')
