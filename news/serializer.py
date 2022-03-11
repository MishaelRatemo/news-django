from dataclasses import field
from rest_framework import serializers
from . models import MoringaMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model =MoringaMerch
        field=('name', 'description', 'price')
        