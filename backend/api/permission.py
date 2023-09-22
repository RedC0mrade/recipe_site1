from rest_framework import permissions


class AuthenticatedOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.user.is_anonymous and view.action == 'me':
            return False
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS or
                obj.author == request.user)


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        pass


class AdminOrReadOnly(permissions.BasePermission):
    """Администратор или безопасный метод."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_staff)
