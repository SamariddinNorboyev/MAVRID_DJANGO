from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # include must point to a valid `users/urls.py`
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)