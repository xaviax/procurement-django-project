from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

# can use a variable with a declared name as the one in tables as it won't query db too much

class IsDepartmentCoordinator(BasePermission):

    def has_permission(self,request,view):
        user = request.user
        return bool(user and user.is_authenticated and user.groups.filter(name=Group.objects.get(pk=1).name).exists())



class IsCreator(BasePermission):

    def has_object_permission(self,request,view,obj):
        return obj.requested_by_id == request.user.id



