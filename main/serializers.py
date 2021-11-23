from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from main.models import Image
from users.models import HexUser


class ImageBaseModelSerializer(HyperlinkedModelSerializer):
    """Serializer for Image"""
    user = PrimaryKeyRelatedField(read_only=True)
    link = serializers.ImageField(write_only=True)

    class Meta:
        model = Image
        fields = ('id', 'link', 'user', 'created_at', )


class ImageModelSerializer(HyperlinkedModelSerializer):
    """Serializer for Image"""
    user = PrimaryKeyRelatedField(read_only=True)
    # images = serializers.SerializerMethodField()

    # def __init__(self, instance=None, data=serializers.empty, images=None,
    #              **kwargs):
    #     super().__init__(instance=instance, data=data, **kwargs)
    #     self.images = images
    #
    # def get_images(self, obj):
    #     id_ = self.context['request'].user.id
    #     user = HexUser.objects
    #     sizes = user.filter(id=id_).values('rate__size')
    #     print(sizes)
    #     self.images = 1
    #     return self.images

    class Meta:
        model = Image
        fields = ('id', 'link', 'user', 'created_at', )
