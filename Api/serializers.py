from rest_framework import serializers

from .models import Cartoon

class CartoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cartoon
        fields = ('name', 'showday')