from rest_framework import serializers
from .models import MyUser
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'id', 'email', 'username', 'full_name', 'phone_number',
            'profile_image', 'language', 'is_verified', 'is_online',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['is_verified', 'is_online', 'created_at', 'updated_at']

class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'id', 'profile_image'
        ]

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'id', 'language'
        ]

    def validate(self, attrs):
        language = attrs.get('language')
        print(language)
        return super().validate(attrs)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)


        if user is None:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("User is deactivated")

        data['user'] = user
        return data