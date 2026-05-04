from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.price} zł)"


class Order(models.Model):
    SIZE_CHOICES = [
        ('S', 'Mała'),
        ('M', 'Średnia'),
        ('L', 'Duża'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='M')
    total_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Zamówienie {self.id} - {self.customer} ({self.get_size_display()})"