# from django.forms import widgets
from rest_framework import serializers
from blogs.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post