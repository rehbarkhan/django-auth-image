from rest_framework import serializers
from .models import VideoFile, VideoDescription

class VideoFileSer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        fields = '__all__'
        extra_kwargs = {
            'uploaded_by' : {'read_only':True},
        }

class VideoDescriptionSer(serializers.ModelSerializer):
    class Meta:
        model = VideoDescription
        fields = '__all__'
        extra_kwargs = {
            'uploaded_by' : {'read_only':True},
            'created_on' : {'read_only':True},
            'updated_on' : {'read_only':True},
        }