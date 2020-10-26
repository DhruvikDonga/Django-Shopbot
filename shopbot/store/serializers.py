from rest_framework import serializers
from .models import Storeitems


class StoreitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storeitems
        fields = '__all__'