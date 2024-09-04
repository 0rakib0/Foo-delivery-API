# from rest_framework.permissions import BasePermission


# class checkRequestMethod(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if(user.is_owner or user.is_employee):
#             return True
#         return False