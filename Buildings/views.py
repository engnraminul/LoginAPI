from email.mime import image
from turtle import title
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from Agent import serializers
from .models import Home, Images
from .serializers import HomeSerializer, HomeDetailsSerializer, ImagesSerializer

from django.db.models import Q, query
from rest_framework.decorators import api_view


class HomeListAPIView(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    serializer_class = HomeSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'

class HomeDetailsAPIView(RetrieveAPIView):
    serializer_class=HomeDetailsSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'


class ImageView(APIView):
    def get(self, request, pk, format=None):
        home=Home.objects.get(pk=pk)
        images=home.images.all()
        serializer = ImagesSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Search(APIView):
    permission_classes=(permissions.AllowAny,)
    def post(self, request, format=None):
        data=self.request.data
        str=data['str']
        q=(Q(title__icontains=str)) | (Q(description__icontains=str))
        queryset=Home.objects.filter(is_published=True)
        queryset=queryset.filter(q)
        serializer=HomeSerializer(queryset, many=True)
        return Response(serializer.data)

#Multiple Search Query

# class Search(APIView):
#     permission_classes=(permissions.AllowAny,)
#     def post(self, request, format=None):
#         data=self.request.data
#         queryset=Home.objects.filter(is_published=True)
#         try:
#             str=data['str']
#             q=(Q(title__icontains=str)) | (Q(description__icontains=str))
#             queryset=queryset.filter(q)
#         except:
#             pass

#         try:
#             price_from=data['price_from']
#             queryset=queryset.filter(price__gte=price_from)
#         except:
#             pass

#         try:
#             price_to=data['price_to']
#             queryset=queryset.filter(price_lte=price_to)
#         except:
#             pass

#         try:
#             city=['city']
#             queryset=queryset.filter(city__iexact=city)
#         except:
#             pass
#         serializer=HomeSerializer(queryset, many=True)
#         return Response(serializer.data)