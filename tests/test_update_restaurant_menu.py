from sources.restaurant_menu import Menu
import pytest

# Paramètres pour le test paramétré
@pytest.mark.parametrize(
    "restaurant_name, item_name, new_description, new_price, expected_result",
    [
        ("KFC", "hot dog", "tinder épicé et sauce hot", 12.50, f"Menu item 'hot dog' updated for KFC."),
        ("Burger", "cheese", "steak et bun au sésame", 9.00, f"Menu item 'cheese' updated for Burger."),
        ("Boulanger", "Panini", "fromage rappé et poulet grillé", 6.50, f"Menu item 'Panini' updated for Boulanger."),
        ("Malifood", "Mafé", "sauce rachide épicée et riz blanc", 12.00, f"Menu item 'Mafé' updated for Malifood.")
    ]
)

@pytest.fixture
def menu_manager_with_item():
    # Crée une instance de Menu
    menu_manager = Menu()

    # Définit le nom du restaurant et le nom de l'élément
    restaurant_name = "KFC"
    item_name = "hot dog"

    # Ajoute un élément au menu avec des valeurs fictives
    menu_manager.add_menu_item(restaurant_name, item_name, "my menu description", 10.00)

    # Renvoie un tuple contenant le gestionnaire de menu, le nom du restaurant et le nom de l'élément ajouté
    return menu_manager, restaurant_name, item_name

def test_update_restaurant_menu(restaurant_name, item_name, new_description, new_price, expected_result):
    # Création d'une instance de la classe Menu
    menu_manager = Menu()

    # Ajout des éléments au menu
    menu_manager.add_menu_item(restaurant_name, item_name, "my menu description", 10.00)

    # Appel de la méthode update_menu_item pour mettre à jour un élément du menu
    result = menu_manager.update_menu_item(restaurant_name, item_name, new_description, new_price)

    # Vérification si l'élément a été correctement mis à jour
    assert result == expected_result

    # Récupération du menu pour le restaurant spécifique
    menu = menu_manager.get_menu(restaurant_name)

    # Vérification si l'élément mis à jour est présent dans le menu
    updated_menu_item = {'item_name': item_name, 'description': new_description, 'price': new_price}
    assert updated_menu_item in menu
