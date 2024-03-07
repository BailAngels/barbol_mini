from django.urls import path

from apps.main.views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about/', AboutPageView.as_view(), name='about')
]

