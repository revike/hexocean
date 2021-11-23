from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from users.models import HexUser
from users.serializers import UserModelSerializer


class UserModelViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """ViewSet for Users"""
    queryset = HexUser.objects.all()
    serializer_class = UserModelSerializer

    def get_queryset(self):
        id_ = self.request.user.id
        if self.queryset.filter(id=id_, is_staff=True):
            return self.queryset
        return self.queryset.filter(id=id_)
