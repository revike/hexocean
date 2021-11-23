from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from main.models import Image
from main.serializers import ImageModelSerializer, ImageBaseModelSerializer
from users.models import HexUser


class ImageModelViewSet(
    ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin,
    GenericViewSet
):
    """ViewSet for Image"""
    queryset = Image.objects.all()
    serializer_class = ImageModelSerializer

    def get_queryset(self):
        id_ = self.request.user.id
        if HexUser.objects.filter(id=id_, is_staff=True):
            return self.queryset
        return self.queryset.filter(user=id_)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        id_ = self.request.user.id
        user = HexUser.objects
        if user.filter(id=id_, rate__link=True):
            return ImageModelSerializer
        return ImageBaseModelSerializer
