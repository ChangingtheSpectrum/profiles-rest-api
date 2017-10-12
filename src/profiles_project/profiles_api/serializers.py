from rest_framework import serializers
from . import models
from django.contrib.auth.models import Group

class HelloSerializer(serializers.Serializer):
	"""Serializes a name field for testing out APIView"""

	name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	""" Serializes user profiles """

	class Meta:
		model = models.UserProfile
		fields = ('id', 'url', 'email', 'name', 'groups', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		""" Create and return a new user """

		user = models.UserProfile(
			email = validated_data['email'],
			name = validated_data['name'],
		)

		user.set_password(validated_data['password'])
		user.save()

		return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')