from django.urls import path
from .views import HomeDetailsAPIView, HomeListAPIView, ImageView

urlpatterns = [
    path('', HomeListAPIView.as_view(), name='home'),
    path('<slug>/', HomeDetailsAPIView.as_view(), name='home-details'),
    path('images/<pk>/', ImageView.as_view(), name='images')
]
