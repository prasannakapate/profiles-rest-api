from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views as view

router = DefaultRouter()
router.register('hello-viewset', view.HelloViewSet, base_name='hello-viewset')
router.register('profile', view.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', view.HelloApiView.as_view()),
    path('login/', view.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]