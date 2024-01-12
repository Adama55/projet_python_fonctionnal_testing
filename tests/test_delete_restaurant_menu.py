from sources.restaurant_menu import Menu
import pytest

# Test pour la méthode delete_menu_item
@pytest.mark.parametrize(
    "restaurant_name, item_name, expected_result",
    [
        ("KFC", "hot dog", f"Menu item 'hot dog' deleted for KFC."),
        ("Burger", "cheese", f"Menu item 'cheese' deleted for Burger."),
        ("Boulanger", "Panini", f"Menu item 'Panini' deleted for Boulanger."),
        ("Malifood", "Mafé", f"Menu item 'Mafé' deleted for Malifood.")
    ]
)
def test_delete_restaurant_menu(restaurant_name, item_name, expected_result):
    # Création d'une instance de la classe Menu
    menu_manager = Menu()

    # Ajout des éléments au menu
    menu_manager.add_menu_item(restaurant_name, item_name, "dummy description", 10.00)

    # Appel de la méthode delete_menu_item pour supprimer un élément du menu
    result = menu_manager.delete_menu_item(restaurant_name, item_name)

    # Vérification si l'élément a été correctement supprimé
    assert result == expected_result

    # Récupération du menu pour le restaurant spécifique
    menu = menu_manager.get_menu(restaurant_name)

    # Vérification si l'élément supprimé n'est plus dans le menu
    deleted_menu_item = {'item_name': item_name, 'description': "dummy description", 'price': 10.00}
    assert deleted_menu_item not in menu
