import pytest
from sources.restaurant_menu import Menu

# Paramètres pour le test paramétré
@pytest.mark.parametrize(
    "restaurant_name, item_name, description, price",
    [
        ("KFC", "hot dog", "tinder et sauce hot", 10.99),
        ("Burger", "cheese", "steak et bun oval", 8.00),
        ("Boulanger", "Panini", "fromage rappé et poulet", 5.50),
        ("Malifood", "Mafé", "sauce rachide et du riz", 10.50)
        # Ajoutez ici d'autres jeux de données pour tester différents scénarios
    ]
)
def test_get_restaurant_menu(menu_manager_with_item,restaurant_name, item_name, description, price):
    menu_manager, _, _ = menu_manager_with_item

    # Ajout des éléments au menu
    menu_manager.add_menu_item(restaurant_name, item_name, description, price)

    # Récupération du menu pour le restaurant spécifique
    menu = menu_manager.get_menu(restaurant_name)

    # Vérification si les menus récupérés contiennent les éléments ajoutés
    expected_menu_item = {'item_name': item_name, 'description': description, 'price': price}
    assert expected_menu_item in menu