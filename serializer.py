from rest_framework import serializers
from .models import user,deposit,withdraw

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
class depositSerializer(serializers.ModelSerializer):
    class Meta:
        model = deposit
        fields = '_all_'
class withdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = withdraw
        fields = '__all__'