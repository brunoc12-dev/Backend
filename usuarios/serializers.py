from rest_framework import serializers
from .models import UserApp

class UserAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserApp
        fields = ('email', 'username','password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
            
            }

    def create(self, validated_data):
        user = UserApp.objects.create(**validated_data)
        return user