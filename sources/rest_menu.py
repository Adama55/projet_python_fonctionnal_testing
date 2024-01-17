class InvalidPriceError(ValueError):
    pass

class DuplicateMenuItemError(ValueError):
    pass

class Menu:
    def __init__(self):
        self.menus ={}
    
    #nouveau
    def add_menu_item(self, restaurant, item_name, description, price):
        if not self._is_valid_price(price):
            raise InvalidPriceError("Invalid price. Please provide a non-negative numeric value.")

        if restaurant not in self.menus:
            self.menus[restaurant] = []

        if self._is_duplicate_item(restaurant, item_name):
            raise DuplicateMenuItemError(f"Menu item '{item_name}' already exists for {restaurant}.")

        self.menus[restaurant].append({'item_name': item_name, 'description': description, 'price': price})
        return f"Menu item '{item_name}' added for {restaurant}."

    def _is_valid_price(self, price):
        return isinstance(price, (int, float)) and price >= 0

    def _is_duplicate_item(self, restaurant, item_name):
        return any(item['item_name'] == item_name for item in self.menus.get(restaurant, []))
    
    #fin
    
    def get_menu(self, restaurant):
        return self.menus.get(restaurant, "Menu not found.")