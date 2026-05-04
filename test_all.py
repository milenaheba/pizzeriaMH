# test_all.py
import menu
import customers
import orders

pizzeria_name = "pizzeria1"

print("=== TEST WSZYSTKICH MODUŁÓW ===\n")

# --- 1. Wczytanie istniejących danych ---
menu.load_menu(pizzeria_name)
customers.load_customers(pizzeria_name)
orders.load_orders(pizzeria_name)

# --- 2. Dodawanie pizzy ---
print("\n--- Dodawanie pizzy ---")
menu.add_pizza("Margherita", 25, pizzeria_name)
menu.add_pizza("Pepperoni", 30, pizzeria_name)
menu.add_pizza("Funghi", 28, pizzeria_name)
menu.list_menu()

# --- 3. Dodawanie klientów ---
print("\n--- Dodawanie klientów ---")
customers.add_customer("Jan Kowalski", "111-222-333", pizzeria_name)
customers.add_customer("Piotr Nowak", "222-333-444", pizzeria_name)
customers.add_customer("Anna Wiśniewska", "333-444-555", pizzeria_name)
customers.list_customers()

# --- 4. Tworzenie zamówień ---
print("\n--- Tworzenie zamówień ---")
order1_id = orders.create_order(1, pizzeria_name)  # Jan Kowalski
order2_id = orders.create_order(2, pizzeria_name)  # Piotr Nowak
order3_id = orders.create_order(99, pizzeria_name) # brak klienta
print()

# --- 5. Dodawanie pozycji do zamówień ---
print("\n--- Dodawanie pozycji ---")
orders.add_item_to_order(order1_id, "Margherita", 2, pizzeria_name)
orders.add_item_to_order(order1_id, "Funghi", 1, pizzeria_name)
orders.add_item_to_order(order2_id, "Pepperoni", 3, pizzeria_name)
orders.add_item_to_order(order2_id, "Hawai", 1, pizzeria_name)  # brak pizzy
print()

# --- 6. Wyświetlanie zamówień ---
print("\n--- Wyświetlanie zamówień ---")
orders.list_order(order1_id)
orders.list_order(order2_id)
orders.list_order(99)  # brak zamówienia

# --- 7. Usuwanie pozycji ---
print("\n--- Usuwanie pozycji ---")
orders.remove_item_from_order(order1_id, "Funghi", pizzeria_name)
orders.remove_item_from_order(order2_id, "Margherita", pizzeria_name)  # brak w zamówieniu
orders.list_order(order1_id)
orders.list_order(order2_id)

# --- 8. Aktualizacja danych klientów ---
print("\n--- Aktualizacja numerów telefonów klientów ---")
customers.update_customer_phone(1, "999-888-777", pizzeria_name)
customers.update_customer_phone(5, "555-666-777", pizzeria_name)  # brak klienta
customers.list_customers()

# --- 9. Aktualizacja cen pizzy ---
print("\n--- Aktualizacja cen pizzy ---")
menu.update_pizza_price("Margherita", 35, pizzeria_name)
menu.update_pizza_price("Hawai", 40, pizzeria_name)  # brak pizzy
menu.list_menu()

# --- 10. Test find_order() ---
print("\n--- Test find_order() ---")
print(orders.find_order(order1_id))  # powinno zwrócić zamówienie
print(orders.find_order(999))        # brak zamówienia