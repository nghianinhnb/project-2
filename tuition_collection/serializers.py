from rest_framework import serializers
from .models import TuitionCollection

class TuitionCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionCollection
        fields = '__all__'
