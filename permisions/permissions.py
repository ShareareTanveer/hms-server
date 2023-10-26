from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and (request.user.role == 'ADMIN')
        return True


class IsAdminAndHROrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and (request.user.role == 'ADMIN' or request.user.role == 'HR')
        return True


class IsAdminAndHROrNothing(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE', 'GET']:
            return request.user.is_authenticated and (request.user.role == 'ADMIN' or request.user.role == 'HR')
        return True


class IsAdminAndAccountantAndReceptionistOrNothing(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated and request.user.role in ['ADMIN', 'ACCOUNTANT', 'RECEPTIONIST']
        elif request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and request.user.role in ['ADMIN', 'ACCOUNTANT']
        else:
            return False


class IsAdminAndReceptionistOrNothing(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and (request.user.role == 'ADMIN' or request.user.role == 'RECEPTIONIST')
        return True


class IsAdminAndReceptionistOrPatient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated and request.user.role in ['ADMIN', 'PATIENT', 'RECEPTIONIST','DOCTOR', 'HR']
        elif request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and request.user.role in ['ADMIN', 'RECEPTIONIST','PATIENT']
        else:
            return False
        
class IsAdminAndReceptionistOrPatientReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated and request.user.role in ['ADMIN', 'PATIENT', 'RECEPTIONIST','HR']
        elif request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and request.user.role in ['ADMIN', 'RECEPTIONIST']
        else:
            return False


class IsAdminAndHROrDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated and request.user.role in ['ADMIN', 'DOCTOR', 'HR', 'RECEPTIONIST']
        elif request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and request.user.role in ['ADMIN', 'HR']
        else:
            return False
