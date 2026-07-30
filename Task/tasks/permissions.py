
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Only allows the user who created a task to view/edit/delete it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user