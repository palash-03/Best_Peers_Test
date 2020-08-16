from django.urls import path
from test_1 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.UserViewSet, basename='user')

urlpatterns = router.urls