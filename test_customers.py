import customers

pizzeria_name = "pizzeria1"

# Wczytanie klientów
customers.load_customers(pizzeria_name)

# Dodawanie klientów
customers.add_customer("Jan Kowalski", "111-222-333", pizzeria_name)
customers.add_customer("Piotr Nowak", "222-333-444", pizzeria_name)
customers.add_customer("Anna Wiśniewska", "333-444-555", pizzeria_name)

# Wyświetlanie klientów
customers.list_customers()

# Znalezienie klienta
cust = customers.find_customer(1)
print("\nZnaleziono klienta:", cust)

cust = customers.find_customer(99)  # brak klienta
print("Znaleziono klienta:", cust)

# Aktualizacja numeru telefonu
customers.update_customer_phone(1, "999-888-777", pizzeria_name)
customers.update_customer_phone(99, "555-666-777", pizzeria_name)  # brak klienta
customers.list_customers()