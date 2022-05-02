from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):

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