from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers, permissions
from rest_framework import viewsets
from .models import UserProfile
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        all_apiviews = [
            "Can use http methods such as get, post, put, delete",
            "similar to traditional django view",
            "Mapped to urls automatically",
            "Gives control of app logic"
        ]

        context = {
            "message": "This shows all we can do with APIViews",
            "all_apiviews": all_apiviews,
        }

        return Response(context)

    def post(self, request):
        """CREATE A NEW MESSAGE"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            context = {
                "message": message
            }

            return Response(context)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """UPDATE A MESSAGE"""
        context = {
            "message": "PUT request"
        }
        return Response(context)

    def patch(self, request, pk=None):
        context = {
            "message": "PATCH request"
        }
        return Response(context)

    def delete(self, request, pk=None):
        context = {
            "message": "Delete request"
        }
        return Response(context)


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializers()

    def list(self, request):

        all_viewsets = [
            "Uses actions such as list, create, update, retrieve",
            "Automatically maps to URLs using routers",
            "Provides more functionality with less code",
        ]
        context = {
            "message": "This shows all we can do with viewsets",
            "all_viewsets": all_viewsets,
        }

        return Response(context)

    def create(self, request):
        """CREATING A NEW MESSAGE"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            context = {
                "message": message
            }
            return Response(context)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        "HANDLE RETRIEVING AN OBJECT BY ID"
        context = {
            "http_method": "GET"
        }

        return Response(context)

    def update(self, request, pk=None):
        """Handle updating an object"""
        context = {
            "http_method": "PUT"
        }

        return Response(context)

    def partial_update(self, request, pk=None):
        """Handle updating a part of an object"""
        context = {
            "http_method": "PATCH"
        }

        return Response(context)

    def destroy(self, request, pk=None):
        """Handle Removing an object"""
        context = {
            "http_method": "Delete"
        }

        return Response(context)


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
