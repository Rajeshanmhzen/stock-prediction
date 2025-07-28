from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'passsword']

    def create(self, validated_data):
        # User.objects..create = save the password ina plain text
        # User.objects.create_user = automatically the hashed passowrd 
        
        # user = User.objects.create_user(**validated_data)
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user