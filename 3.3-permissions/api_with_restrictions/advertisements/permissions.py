from rest_framework.authtoken.admin import User
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """Даем разрешение на изменение только владельцу объявления, остальные только просматривают"""
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user in User.objects.filter(is_superuser=True):
            return True
        return request.user == obj.creator