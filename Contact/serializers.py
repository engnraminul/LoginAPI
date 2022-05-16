from dataclasses import fields
from rest_framework import serializers
from Contact.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'