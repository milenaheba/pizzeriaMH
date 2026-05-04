import menu

pizzeria_name = "pizzeria1"

# Wczytanie menu
menu.load_menu(pizzeria_name)

# Dodawanie pizzy
menu.add_pizza("Margherita", 25, pizzeria_name)
menu.add_pizza("Pepperoni", 30, pizzeria_name)
menu.add_pizza("Funghi", 28, pizzeria_name)

# Wyświetlanie menu
menu.list_menu()

# Szukanie pizzy
pizza = menu.find_pizza("Margherita")
print("\nZnaleziono:", pizza)

pizza = menu.find_pizza("Hawai")  # brak pizzy
print("Znaleziono:", pizza)

# Aktualizacja ceny
menu.update_pizza_price("Margherita", 35, pizzeria_name)
menu.update_pizza_price("Hawai", 40, pizzeria_name)  # brak pizzy
menu.list_menu()