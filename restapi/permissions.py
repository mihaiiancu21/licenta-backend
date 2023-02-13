from rest_framework.permissions import IsAuthenticated


def get_permission_class(default, get=None, post=None, patch=None, put=None, delete=None):
    perm_map = {'GET': get or default,
                'POST': post or default,
                'PATCH': patch or default,
                'PUT': put or default,
                'DELETE': delete or default,
                }

    class PermissionClass(object):

        def has_permission(self, request, view):
            permission_classes = perm_map.get(request.method, default)
            if isinstance(permission_classes, list):
                for permission_class in permission_classes:
                    if permission_class().has_permission(request, view):
                        # if at least one permission is True in the list we return True
                        return True
            else:
                permission_class = permission_classes
                return permission_class().has_permission(request, view)
            return False

        def has_object_permission(self, request, view, obj):
            permission_classes = perm_map.get(request.method, default)
            if isinstance(permission_classes, list):
                for permission_class in permission_classes:
                    if permission_class().has_object_permission(request, view, obj):
                        # if at least one permission is True in the list we return True
                        return True
            else:
                permission_class = permission_classes
                return permission_class().has_object_permission(request, view, obj)
            return False

    return PermissionClass,


class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        if not super(IsStaff, self).has_permission(request, view):
            return False
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if not super(IsStaff, self).has_permission(request, view):
            return False
        return request.user.is_staff
