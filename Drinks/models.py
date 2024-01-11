from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.PositiveIntegerField()

class Category(models.Model):
    name = models.CharField(max_length=50)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    is_available = models.BooleanField(default=True)
    volume = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # image = models.ImageField(upload_to='drink_images/', null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.description

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    drinks = models.ManyToManyField(Drink)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} {self.drinks.name}(s) in Order {self.order.id}"
