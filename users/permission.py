from rest_framework.permissions import BasePermission



# create custom permission for creat data by api for employ and woner
class checkUserRaol(BasePermission):
    def has_permission(self, request, view):
        user = request.user  
        if(user.user_role == "owner" or user.user_role == "employ"):
            return True
        return False