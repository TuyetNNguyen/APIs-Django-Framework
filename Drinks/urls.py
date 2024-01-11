# urls.py
from django.contrib import admin
from django.urls import path
from Drinks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', views.drink_list),
    path('drinks/<int:id>/', views.drink_detail),
    path('customers/', views.customer_list),
    path('categories/', views.category_list),
    path('ingredients/', views.ingredient_list),
    path('orders/', views.order_list),
    path('reviews/', views.review_list),
    path('orderitems/', views.order_item_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
