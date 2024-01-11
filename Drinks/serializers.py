# serializers.py
from rest_framework import serializers
from .models import Customer, Category, Ingredient, Drink, Order, Review, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class DrinkSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Drink
        fields = ['id', 'name', 'price', 'description', 'category', 'ingredients', 'is_available', 'volume']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_date']

class ReviewSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    drink = DrinkSerializer()

    class Meta:
        model = Review
        fields = ['id', 'customer', 'drink', 'rating', 'review_text', 'review_date']

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    drinks = DrinkSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'drinks', 'quantity']
