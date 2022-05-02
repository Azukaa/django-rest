from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializers
# Create your views here.


class HelloApiView(APIView):
    serializer_class = HelloSerializers

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
