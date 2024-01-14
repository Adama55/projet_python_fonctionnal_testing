from sources.restaurant_menu import Menu
import pytest

# Fixture pour créer une instance de Menu et ajouter un élément au menu
@pytest.fixture
def menu_manager_with_item():
    menu_manager = Menu()
    restaurant_name = "KFC"
    item_name = "hot dog"
    menu_manager.add_menu_item(restaurant_name, item_name, "dummy description", 10.00)
    return menu_manager, restaurant_name, item_name

# Test pour la méthode delete_menu_item
@pytest.mark.usefixtures("menu_manager_with_item")
@pytest.mark.parametrize(
    "restaurant_name, item_name, expected_result",
    [
        ("KFC", "hot dog", f"Menu item 'hot dog' deleted for KFC.")
        #("Burger", "cheese", f"Menu item 'cheese' deleted for Burger."),
        #("Boulanger", "Panini", f"Menu item 'Panini' deleted for Boulanger."),
        #("Malifood", "Mafé", f"Menu item 'Mafé' deleted for Malifood.")
    ]
)
def test_delete_restaurant_menu(menu_manager_with_item, restaurant_name, item_name, expected_result):
    menu_manager_with_item_result = menu_manager_with_item
    menu_manager, _, _ = menu_manager_with_item_result

    # Appel de la méthode delete_menu_item pour supprimer un élément du menu
    result = menu_manager.delete_menu_item(restaurant_name, item_name)

    # Vérification si l'élément a été correctement supprimé
    assert result == expected_result

    # Récupération du menu pour le restaurant spécifique
    menu = menu_manager.get_menu(restaurant_name)

    # Vérification si l'élément supprimé n'est plus dans le menu
    deleted_menu_item = {'item_name': item_name, 'description': "dummy description", 'price': 10.00}
    assert deleted_menu_item not in menu
