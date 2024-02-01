from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from taxi.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("taxi/", include("taxi.urls", namespace="taxi"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
