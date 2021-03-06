from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or request.user
            and request.user.is_staff
        )


class IsSuperUserOrStaffReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Access to user staff
        if request.method in permissions.SAFE_METHODS and request.user.is_staff:
            return True
        # Access to superuser
        return bool(
            request.user.is_authenticated and request.user.is_superuser
        )


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(
            # access to superuser
            request.user.is_authenticated and request.user.is_superuser
            # access to author
            or obj.author == request.user
        )
