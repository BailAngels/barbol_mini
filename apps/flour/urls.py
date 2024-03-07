from django.urls import path

from apps.flour.views import FlourListView, FlourDetailView

urlpatterns = [
    path('flours/', FlourListView.as_view(), name='flour_list'),
    path('flours/<int:pk>/', FlourDetailView.as_view(), name='flour_detail'),
]
