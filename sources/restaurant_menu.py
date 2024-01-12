class Menu:
    def __init__(self):
        self.menus ={}
    
    def add_menu_item(self, restaurant, item_name, description, price):
        if restaurant not in self.menus:
            self.menus[restaurant] = []
        self.menus[restaurant].append({'item_name': item_name, 'description': description, 'price': price})
        return f"Menu item '{item_name}' added for {restaurant}."
    
    def get_menu(self, restaurant):
        return self.menus.get(restaurant, "Menu not found.")
    
    def update_menu_item(self, restaurant, item_name, new_description, new_price):
        if restaurant not in self.menus:
            return "Menu not found."
        for item in self.menus[restaurant]:
            if item['item_name'] == item_name:
                item['description'] = new_description
                item['price'] = new_price
                return f"Menu item '{item_name}' updated for {restaurant}."
        return "Menu item not found."
    
    def delete_menu_item(self, restaurant, item_name):
        if restaurant not in self.menus:
            return "Menu not found."
        for item in self.menus[restaurant]:
            if item['item_name'] == item_name:
                self.menus[restaurant].remove(item)
                return f"Menu item '{item_name}' deleted for {restaurant}."
        return "Menu item not found."