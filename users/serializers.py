from rest_framework.serializers import HyperlinkedModelSerializer
from users.models import HexUser, RateUser, SizeImage


class SizeImageModelSerializer(HyperlinkedModelSerializer):
    """Serializer for size image"""

    class Meta:
        model = SizeImage
        fields = ('name', )


class UserRateModelSerializer(HyperlinkedModelSerializer):
    """Serializer for Rate"""
    size = SizeImageModelSerializer(many=True)

    class Meta:
        model = RateUser
        fields = ('name', 'link', 'size', 'expiration', )


class UserModelSerializer(HyperlinkedModelSerializer):
    """Serializer for users"""
    rate = UserRateModelSerializer()

    class Meta:
        model = HexUser
        fields = ('id', 'url', 'username', 'rate')
