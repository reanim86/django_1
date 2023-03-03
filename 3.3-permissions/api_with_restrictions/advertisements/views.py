from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """Описываем viewset для работы с моделью Advertisement"""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AdvertisementFilter

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        return []

    @action(methods=['patch'], detail=True)
    def favourites(self, request, pk=None):
        """Добавление объявления в избранное"""
        user = User.objects.get(pk=pk)
        Advertisement.objects.add(favourites=user)
        # Advertisement.objects.filter(pk=pk).add(favourites=request.user)
        return Response('Запись добавлена в избранное')
