import menu
import customers
import orders

pizzeria_name = "pizzeria1"

# --- Wczytanie danych ---
menu.load_menu(pizzeria_name)
customers.load_customers(pizzeria_name)
orders.load_orders(pizzeria_name)

# --- Przygotowanie danych ---
menu.add_pizza("Margherita", 25, pizzeria_name)
menu.add_pizza("Pepperoni", 30, pizzeria_name)
customers.add_customer("Jan Kowalski", "111-222-333", pizzeria_name)
customers.add_customer("Piotr Nowak", "222-333-444", pizzeria_name)

# --- Tworzenie zamówień ---
order1_id = orders.create_order(1, pizzeria_name)
order2_id = orders.create_order(2, pizzeria_name)

# --- Dodawanie pozycji ---
orders.add_item_to_order(order1_id, "Margherita", 2, pizzeria_name)
orders.add_item_to_order(order1_id, "Pepperoni", 1, pizzeria_name)
orders.add_item_to_order(order2_id, "Pepperoni", 3, pizzeria_name)

# --- Wyświetlanie zamówień ---
orders.list_order(order1_id)
orders.list_order(order2_id)

# --- Usuwanie pozycji ---
orders.remove_item_from_order(order1_id, "Pepperoni", pizzeria_name)
orders.list_order(order1_id)