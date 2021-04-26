from rest_framework import serializers

from .models import Account


class DepositeSerializer(serializers.Serializer):
    class Meta:
        model = Account
        fields = 'amount'
