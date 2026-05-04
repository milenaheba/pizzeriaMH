import json
import os

customers = []
next_customer_id = 1

# --- Zapis i odczyt ---
def save_customers(pizzeria_name):
    os.makedirs("data", exist_ok=True)
    data = {'customers': customers, 'next_customer_id': next_customer_id}
    with open(f"data/{pizzeria_name}_customers.json", "w") as f:
        json.dump(data, f, indent=2)

def load_customers(pizzeria_name):
    global customers, next_customer_id
    path = f"data/{pizzeria_name}_customers.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
            customers = data.get('customers', [])
            next_customer_id = data.get('next_customer_id', 1)
    else:
        customers = []
        next_customer_id = 1

# --- Funkcje operacyjne ---
def add_customer(name, phone, pizzeria_name):
    global next_customer_id

    name = name.strip().title()
    phone = phone.strip()

    # 🔒 blokada duplikatu po telefonie
    if find_customer_by_phone(phone):
        print("Klient z tym numerem telefonu już istnieje!")
        return False

    customer = {
        'id': next_customer_id,
        'name': name,
        'phone': phone
    }

    customers.append(customer)
    print(f"Dodano klienta: id {next_customer_id}, {name}")

    next_customer_id += 1
    save_customers(pizzeria_name)

    return customer['id']

def find_customer(customerID):
    for customer in customers:
        if customer['id'] == customerID:
            return customer
    return None

def find_customer_by_phone(phone):
    phone = phone.strip()

    for customer in customers:
        if customer['phone'] == phone:
            return customer
    return None

def list_customers():
    if not customers:
        print("Lista klientów jest pusta")
        return
    print("=== KLIENCI ===")
    for customer in customers:
        print(f"[{customer['id']}] {customer['name']} - {customer['phone']}")

def update_customer_phone(customerID, new_phone, pizzeria_name):
    customer = find_customer(customerID)
    if not customer:
        print(f"Nie znaleziono klienta o ID {customerID}")
        return False
    customer['phone'] = new_phone
    print(f"Zaktualizowano numer telefonu klienta {customerID} na {new_phone}")
    save_customers(pizzeria_name)
    return True