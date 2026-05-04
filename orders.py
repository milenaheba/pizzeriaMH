import json
import os
import customers
import menu

orders = []
next_order_id = 1

# --- Zapis i odczyt ---
def save_orders(pizzeria_name):
    os.makedirs("data", exist_ok=True)
    data = {"orders": orders, "next_order_id": next_order_id}
    with open(f"data/{pizzeria_name}_orders.json", "w") as f:
        json.dump(data, f, indent=2)

def load_orders(pizzeria_name):
    global orders, next_order_id
    path = f"data/{pizzeria_name}_orders.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
            orders = data.get("orders", [])
            next_order_id = data.get("next_order_id", 1)
    else:
        orders = []
        next_order_id = 1

# --- Funkcje operacyjne ---
def create_order(customerID, pizzeria_name):
    global next_order_id
    cust = customers.find_customer(customerID)
    if not cust:
        print(f"Podany klient o ID {customerID} nie istnieje")
        return False
    order = {'id': next_order_id, 'customer_id': customerID, 'items': []}
    orders.append(order)
    print(f"Dodano zamówienie ID {next_order_id} dla klienta {customerID}")
    next_order_id += 1
    save_orders(pizzeria_name)
    return order['id']

def find_order(order_id):
    for order in orders:
        if order['id'] == order_id:
            return order
    print(f"Nie znaleziono zamówienia o ID {order_id}")
    return None

def add_item_to_order(order_id, pizza_name, quantity, pizzeria_name):
    # Znajdź zamówienie
    order = find_order(order_id)
    if not order:
        print(f"Nie znaleziono zamówienia ID {order_id}")
        return False

    # Znajdź pizzę w menu (case-insensitive)
    pizza = menu.find_pizza(pizza_name)
    if not pizza:
        print(f"Nie znaleziono pizzy {pizza_name}")
        return False

    # Normalizacja nazwy pizzy
    pizza_name_normalized = pizza['name']

    # Sprawdź, czy pizza już jest w zamówieniu
    for item in order['items']:
        if item['pizza_name'].lower() == pizza_name_normalized.lower():
            item['quantity'] += quantity
            print(f"Dodano {quantity} x {pizza_name_normalized} (suma w zamówieniu: {item['quantity']})")
            save_orders(pizzeria_name)
            return True

    # Jeśli pizza nie była wcześniej w zamówieniu, dodaj nową pozycję
    order['items'].append({
        'pizza_name': pizza_name_normalized,
        'price': pizza['price'],
        'quantity': quantity
    })

    print(f"Dodano {quantity} x {pizza_name_normalized}")
    save_orders(pizzeria_name)
    return True

def list_order(order_id):
    order = find_order(order_id)
    if not order:
        return
    print(f"=== ZAMÓWIENIE ID {order_id} ===")
    print(f"Klient ID: {order['customer_id']}")
    total = 0
    if not order['items']:
        print("Brak pozycji w zamówieniu")
    else:
        for item in order['items']:
            subtotal = item['price'] * item['quantity']
            print(f"{item['quantity']} x {item['pizza_name']} = {subtotal:.2f} zł")
            total += subtotal
    print(f"RAZEM: {total:.2f} zł")

def remove_item_from_order(order_id, pizza_name, pizzeria_name):
    # Znajdź zamówienie
    order = find_order(order_id)
    if not order:
        print(f"Nie znaleziono zamówienia ID {order_id}")
        return False

    # Normalizacja nazwy pizzy
    pizza_name_normalized = pizza_name.strip().lower()

    # Szukamy pozycji w zamówieniu (case-insensitive)
    for i, item in enumerate(order['items']):
        if item['pizza_name'].lower() == pizza_name_normalized:
            removed_item = order['items'].pop(i)
            print(f"Usunięto {removed_item['pizza_name']} z zamówienia ID {order_id}")
            save_orders(pizzeria_name)
            return True

    print(f"Nie znaleziono pizzy {pizza_name} w zamówieniu ID {order_id}")
    return False