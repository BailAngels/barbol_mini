from django.urls import path
from apps.cakes.views import CakeListView, CakeDetailView


urlpatterns = [
    path('cakes/', CakeListView.as_view(), name='cake_list'),
    path('cakes/<int:pk>/', CakeDetailView.as_view(), name='cake_detail')
]
