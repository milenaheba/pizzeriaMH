from django.shortcuts import render, redirect
from .models import Customer, Pizza, Order


def home(request):
    pizzas = Pizza.objects.all()
    orders = Order.objects.all().order_by("-created_at")

    return render(request, "pizzeria/home.html", {
        "pizzas": pizzas,
        "orders": orders,
    })


def create_order(request):
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        pizza_ids = request.POST.getlist("pizzas")
        size = request.POST.get("size")

        size_prices = {
            "S": 0,
            "M": 5,
            "L": 10,
        }

        if customer_name and pizza_ids:
            customer, created = Customer.objects.get_or_create(name=customer_name)

            selected_pizzas = Pizza.objects.filter(id__in=pizza_ids)

            total_price = sum(pizza.price for pizza in selected_pizzas)
            total_price += size_prices.get(size, 0) * selected_pizzas.count()

            order = Order.objects.create(
                customer=customer,
                size=size,
                total_price=total_price
            )

            order.pizzas.set(selected_pizzas)

        return redirect("home")

    pizzas = Pizza.objects.all()
    return render(request, "pizzeria/create_order.html", {
        "pizzas": pizzas,
    })

from django.shortcuts import get_object_or_404

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect("home")