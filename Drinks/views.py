from .models import Drink
from django.http import JsonResponse
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Category, Ingredient, Drink, Order, Review, OrderItem
from .serializers import (
    CustomerSerializer,
    CategorySerializer,
    IngredientSerializer,
    DrinkSerializer,
    OrderSerializer,
    ReviewSerializer,
    OrderItemSerializer,
)


# CRUD
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()  # GET all the drinks
        serializer = DrinkSerializer(drinks, many=True)  # serializer them
        return Response(serializer.data)  # return JsonResponse

    elif request.method == 'POST':  # add data into db
        serializer = DrinkSerializer(data=request.data)  # deserialize them
        if serializer.is_valid():
            serializer.save()  # create a drink object
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # return Response
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id) # GET all the drink by id
    except Drink.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink) # serialize it
        return Response(serializer.data)
    elif request.method == 'PUT': # update db
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response({"customers": serializer.data})

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response({"categories": serializer.data})

@api_view(['GET'])
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response({"ingredients": serializer.data})

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response({"orders": serializer.data})

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response({"reviews": serializer.data})

@api_view(['GET'])
def order_item_list(request):
    order_items = OrderItem.objects.all()
    serializer = OrderItemSerializer(order_items, many=True)
    return Response({"order_items": serializer.data})
