from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem


class HelloSerializers(serializers.Serializer):
    """A name field for testing APIView. They perform similarly to django forms. Used for Post and Put"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    "Serializes a User profile object"

    class Meta:
        model = UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"]
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer for Profile feed"""

    class Meta:
        model = ProfileFeedItem
        fields = ("id", "user_profile", "status_text", "date_created")
        extra_kwargs = {
            "user_profile": {
                "read_only": True
            }
        }
