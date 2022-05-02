from django.urls import path, include
from .views import HelloApiView, HelloViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, basename="hello-viewset")
urlpatterns = [
    path("hello-view", HelloApiView.as_view(), name="hello-view"),
    path("", include(router.urls))
]
