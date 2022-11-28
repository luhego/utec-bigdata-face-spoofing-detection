from rest_framework import serializers

from django.contrib.auth import get_user_model, password_validation

User = get_user_model()


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "genre",
            "video_s3_url",
        )

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64, required=True)
    password = serializers.CharField(max_length=128, required=True)
    video_s3_url = serializers.CharField(max_length=100, required=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                data["user"] = user
            else:
                raise serializers.ValidationError("Incorrect credentials")
        else:
            raise serializers.ValidationError("Must provide username and password")
        return data
