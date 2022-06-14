from rest_framework.permissions import BasePermission

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            user = request.user
            if hasattr(user, 'is_anonymous') and user.is_anonymous:
                return True  # Change to False
            elif user.is_admin:
                return True
            elif request.method in SAFE_METHODS and user.is_authenticated:
                return True
        return False
