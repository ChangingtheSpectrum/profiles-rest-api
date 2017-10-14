from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
	""" Allows users to edit own profiles """

	def has_object_permission(self, request, view, obj):
		"""Check user trying to edit their own profile."""

		if request.method in permissions.SAFE_METHODS:
			return True
	
		return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
	""" Allows users to post a status """

	def has_object_permission(self, request, view, obj):
		"""Check to see if user is logged in"""

		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.user_profile.id == request.user.id