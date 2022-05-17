from cgitb import lookup
from dataclasses import fields
from rest_framework import serializers
from .models import Home, Images

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('Title', 'slug', 'bathrooms', 'bedrooms', 'sale_type'. 'home_type', 'open_house', 'description', 'city', 'state', 'zipcode', 'address', 'photo')

class HomeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        lookup_field = 'slug'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
        lookup_field = 'home'