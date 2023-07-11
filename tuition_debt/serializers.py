from rest_framework import serializers
from .models import TuitionDebt

class TuitionDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionDebt
        fields = '__all__'
