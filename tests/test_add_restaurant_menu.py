from sources.restaurant_menu import Menu 
import pytest

@pytest.mark.parametrize(
    "restaurant_name, item_name, description, price, expected_result",
    [
        ("KFC", "hot dog", "tinder et sauce hot", 10.99, 
         f"Menu item 'hot dog' added for KFC."),

        ("Burger", "cheese", "steak et bun oval", 8.00, 
         f"Menu item 'cheese' added for Burger."),

        ("Boulanger", "Panini", "fromage rappé et poulet", 5.50, 
         f"Menu item 'Panini' added for Boulanger."),

        ("Malifood", "Mafé", "sauce rachide et du riz", 10.50, 
         f"Menu item 'Mafé' added for Malifood.")
        
    ]
)
def test_add_menu_item(restaurant_name, item_name, description, price,expected_result):
    # Création d'une instance de la classe Menu
    menu_manager = Menu()

    # Appel de la méthode add_menu_item pour ajouter un élément au menu
    result = menu_manager.add_menu_item(restaurant_name, item_name, description, price)

    # Vérification si l'élément a été correctement ajouté
    assert result == expected_result 
    #f"Menu item '{item_name}' added for {restaurant_name}."

    # Vérification si l'élément ajouté se trouve réellement dans le menu
    menu = menu_manager.get_menu(restaurant_name)
    expected_menu_item = {'item_name': item_name, 'description': description, 'price': price}
    assert expected_menu_item in menu
