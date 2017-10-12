from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
	""" Allows users to edit own profiles """

	def has_object_permission(self, request, view, obj):
		"""Check user trying to edit their own profile."""

		if request.method in permissions.SAFE_METHODS:
			return True
	
