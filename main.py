"""
Główny plik aplikacji pizzerii – wersja CLI
"""

import menu
import customers
import orders


def cli():
    print("=== APLIKACJA PIZZERII (CLI) ===\n")

    pizzeria_name = "pizzeria1"

    # Wczytanie danych
    menu.load_menu(pizzeria_name)
    customers.load_customers(pizzeria_name)
    orders.load_orders(pizzeria_name)

    while True:
        print("\n====== MENU GŁÓWNE ======")
        print("1. Dodaj pizzę")
        print("2. Dodaj klienta")
        print("3. Nowe zamówienie")
        print("4. Wyświetl menu")
        print("5. Wyświetl klientów")
        print("6. Wyświetl zamówienie")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        # Dodaj pizzę
        if choice == "1":
            name = input("Nazwa pizzy: ")
            price = float(input("Cena: "))
            menu.add_pizza(name, price, pizzeria_name)

        # Dodaj klienta
        elif choice == "2":
            name = input("Imię i nazwisko: ")
            phone = input("Telefon: ")
            customers.add_customer(name, phone, pizzeria_name)

        # Nowe zamówienie
        elif choice == "3":
            try:
                customerID = int(input("Podaj ID klienta: "))
                order_id = orders.create_order(customerID, pizzeria_name)

                if order_id:
                    while True:
                        pizza_name = input("Nazwa pizzy (ENTER aby zakończyć): ")
                        if pizza_name == "":
                            break
                        quantity = int(input("Ilość: "))
                        orders.add_item_to_order(order_id, pizza_name, quantity, pizzeria_name)

            except ValueError:
                print("Błędne dane.")

        # Wyświetl menu
        elif choice == "4":
            menu.list_menu()

        # Wyświetl klientów
        elif choice == "5":
            customers.list_customers()

        # Wyświetl zamówienie
        elif choice == "6":
            try:
                order_id = int(input("Podaj ID zamówienia: "))
                orders.list_order(order_id)
            except ValueError:
                print("Błędne ID.")

        # Wyjście
        elif choice == "0":
            print("Zamykanie aplikacji...")
            break

        else:
            print("Niepoprawna opcja!")


if __name__ == "__main__":
    cli()