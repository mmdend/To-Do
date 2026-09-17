from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150, validators=[]
    )  # Showing serializer username validation error first
    email = serializers.EmailField(validators=[])
    password1 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password1",
        )

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")

        return value

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("This email is already registered.")

        return value

    def validate(self, attrs):
        password = attrs.get("password")
        password1 = attrs.get("password1")
        if password != password1:
            raise serializers.ValidationError({"password": "Passwords must match."})
        try:
            validate_password(password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        return User.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        data["email"] = self.user.email
        return data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        new_password1 = attrs.get("new_password1")
        if new_password != new_password1:
            raise serializers.ValidationError({"detail": "Passwords must match."})
        try:
            validate_password(new_password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})

        return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
        )
