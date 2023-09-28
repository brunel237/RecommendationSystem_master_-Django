from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # id = serializers.CharField(read_only=True )
    password = serializers.CharField(write_only=True )
    registration_number = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            # 'id',
            'first_name', 
            'last_name', 
            'age',
            'date_of_birth', 
            'email', 
            'phone_number', 
            'sex', 
            'address', 
            'email', 
            'registration_number', 
            'username', 
            'password',
            'profile_picture'
        ]
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(make_password(password))
        user.save()
        
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(make_password(password))
        instance.save()
        
        return instance