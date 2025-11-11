from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required=True)
    
    class Meta:
        model = User
        fields = ['username','email', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(write_only = True, required = True)
    
        
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("user is deactivated")
                data['user'] = user
            else:
                raise serializers.ValidationError("Invalid Credentials")
        else:
            raise serializers.ValidationError("Both fields are Required")
        
        return data        