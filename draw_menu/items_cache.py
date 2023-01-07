from draw_menu.models import MenuItem


class ItemsCache:
    def __init__(self):
        self.cache_dict = {}

    def delete_items(self, key):
        self.cache_dict.pop(key, None)

    def get_or_set_items(self, menu_name):
        if menu_name not in self.cache_dict:
            list_items = list(MenuItem.objects.filter(menu_id__menu_name=menu_name).values())
            self.cache_dict[menu_name] = list_items
            return self.cache_dict[menu_name]
        return self.cache_dict[menu_name]


cache_item = ItemsCache()
