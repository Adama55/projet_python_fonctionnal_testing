from sources.restaurant_menu import Menu 

def test_add_menu_item():
    # Création d'une instance de la classe Menu
    menu_manager = Menu()

    # Paramètres pour l'ajout d'un élément au menu
    restaurant_name = "Mon Restaurant"
    item_name = "Plat du jour"
    description = "Délicieux plat principal"
    price = 15.99

    # Appel de la méthode add_menu_item pour ajouter un élément au menu
    result = menu_manager.add_menu_item(restaurant_name, item_name, description, price)

    # Vérification si l'élément a été correctement ajouté
    assert result == f"Menu item '{item_name}' added for {restaurant_name}."

    # Vérification si l'élément ajouté se trouve réellement dans le menu
    menu = menu_manager.get_menu(restaurant_name)
    expected_menu_item = {'item_name': item_name, 'description': description, 'price': price}
    assert expected_menu_item in menu
