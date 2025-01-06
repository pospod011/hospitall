from rest_framework import permissions
from .models import PatientProfile, Doctor




class CheckDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, Doctor) and user.role == 'врач':
            return True
        return False


class CheckPatient(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, PatientProfile) and user.role == 'пациент':
            return True
        return False


class CheсkReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.patient == request.user


