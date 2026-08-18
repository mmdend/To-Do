from rest_framework import permissions


# For public tasks -> feature for future
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsOwner(permissions.BasePermission):
    """
    Only allow users to manage their own tasks.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
