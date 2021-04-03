from .models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('last_name', 'first_name')
