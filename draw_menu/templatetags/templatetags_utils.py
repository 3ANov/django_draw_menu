def group_by_menu_items(menu_items, current_url):
    menu_items.insert(0, {'parent_menu_item_id': -1, 'id': 'root', 'link': -1})

    for item in menu_items:
        item['children'] = []
        item['active_flag'] = False

    for i in menu_items:
        if i['parent_menu_item_id'] is None:
            i['parent_menu_item_id'] = 'root'

    result_dict = menu_items[0]

    def insert(tree, node):
        if node["link"] == current_url:
            node["active_flag"] = True
        if node["parent_menu_item_id"] == tree["id"]:
            if "children" not in tree:
                tree["children"] = [node]
            else:
                tree["children"].append(node)
        elif "children" in tree:
            for c in tree["children"]:
                insert(c, node)

    for record in menu_items:
        insert(result_dict, record)

    return result_dict['children']
