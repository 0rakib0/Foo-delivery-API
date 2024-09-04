from rest_framework.permissions import BasePermission


class checkUserRaol(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if(user.user_role == "owner" or user.user_role == "employ"):
            return True
        return False