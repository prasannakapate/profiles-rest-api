from django.urls import path
from profiles_api import views as view

urlpatterns = [
    path('hello-view/', view.HelloApiView.as_view()),
]