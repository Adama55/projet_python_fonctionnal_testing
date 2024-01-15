from sources.restaurant_menu import Menu
import pytest

# Fixture pour créer une instance de Menu et ajouter un élément au menu
@pytest.fixture(params=[
    ("KFC", "hot dog"),
    ("Burger", "cheese"),
    ("Boulanger", "Panini"),
    ("Malifood", "Mafé")
])
def menu_manager_with_item(item_name,restaurant_name):
    menu_manager = Menu()
    menu_manager.add_menu_item(restaurant_name, item_name, "my menu description", 10.00)
    return menu_manager, restaurant_name, item_name
