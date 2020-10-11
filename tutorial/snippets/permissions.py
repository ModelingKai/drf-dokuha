from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request.
        # so we'll always allow GET, HEAD or OPTIONS requests
        is_safe = request.method in permissions.SAFE_METHODS
        if is_safe:
            return True

        # Write permission are onlly allowed to the owner of the snippet.
        is_unsafe = obj.owner == request.user
        return is_unsafe
