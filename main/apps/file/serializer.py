from rest_framework import serializers
from .models import File, FileGroup



class FileGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileGroup
        fields = (
        'id', 
        'author',
        'name'
        )


class FileLitSerializer(serializers.ModelSerializer):
    group = FileGroupSerializer()

    class Meta:
        model = File
        fields = (
            'id', 
            'name', 
            'file', 
            'shared_with', 
            'group'
        )


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'name', 
            'file', 
            'shared_with', 
            'group'
        )