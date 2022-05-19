from rest_framework import serializers

from .models import Book

# class BookSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=120)
#     bookId = serializers.IntegerField()
#     date = serializers.DateTimeField()
#     author = serializers.CharField(max_length=120)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'