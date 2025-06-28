from django.urls import path, include
from .views import LoginView, MeView, LanguageAPIView
from .views import ProfileImageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'image', ProfileImageViewSet, basename='image')


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('me/', MeView.as_view(), name='me'),
    path('', include(router.urls)),
    path('language/', LanguageAPIView.as_view(), name='language'),
]
