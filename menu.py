import json
import os

menu = []

# --- Zapis i odczyt ---
def save_menu(pizzeria_name):
    os.makedirs("data", exist_ok=True)
    with open(f"data/{pizzeria_name}_menu.json", "w") as f:
        json.dump(menu, f, indent=2)

def load_menu(pizzeria_name):
    global menu
    path = f"data/{pizzeria_name}_menu.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            menu = json.load(f)
    else:
        menu = []

# --- Funkcje operacyjne ---
def add_pizza(name, price, pizzeria_name):

    name = name.strip().title()

    if find_pizza(name):
        print("Taka pizza już istnieje!")
        return False

    pizza = {
        'name': name,
        'price': float(price)
    }

    menu.append(pizza)
    print(f"Dodano {name} za {price}zł")
    save_menu(pizzeria_name)

    return True

def list_menu():
    if not menu:
        print("Menu jest puste!")
        return
    print("===== MENU =====")
    for pizza in menu:
        print(f"- {pizza['name']}: {pizza['price']:.2f} zł")

def find_pizza(name):
    for pizza in menu:
        if pizza['name'].lower == name.lower():
            return pizza
    return None

def update_pizza_price(name, new_price, pizzeria_name):
    pizza = find_pizza(name)
    if not pizza:
        print(f"Brak pizzy '{name}'")
        return False
    pizza['price'] = float(new_price)
    print(f"Cena pizzy '{name}' zmieniona na {new_price}zł")
    save_menu(pizzeria_name)
    return True