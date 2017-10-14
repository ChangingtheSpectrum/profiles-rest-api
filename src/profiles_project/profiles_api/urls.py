from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('group', views.GroupViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('profile-feed-item', views.ProfileFeedItemViewSet)

urlpatterns = [
	url(r'^hello-view/', views.HelloApiView.as_view()),
	url(r'', include(router.urls)),
]