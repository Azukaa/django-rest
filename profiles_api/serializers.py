import re
from typing_extensions import Required
from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """A name field for testing APIView. They perform similarly to django forms. Used for Post and Put"""
    name = serializers.CharField(max_length=10)
