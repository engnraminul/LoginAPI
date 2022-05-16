from django.urls import path
from .views import ContactAPIView


urlpatterns = [
    path('api/', ContactAPIView.as_view()),
]
