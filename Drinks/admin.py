from django.contrib import admin
from .models import Customer, Category, Ingredient, Drink, Order, Review, OrderItem

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Drink)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(OrderItem)
