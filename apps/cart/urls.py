from django.urls import path
from apps.cart.views import CartListViews, QuantityChangeLogics

urlpatterns = [
    path('cart', CartListViews.as_view(), name='cart_list'),
    path('minus/<int:pk>/', QuantityChangeLogics.minus_quantity, name='minus_quantity'),
    path('plus/<int:pk>/', QuantityChangeLogics.plus_quantity, name='plus_quantity')
]
