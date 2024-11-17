from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include
schema_view = get_schema_view(
    openapi.Info(
        title="Students Registration API",
        default_version="v1",
        description="Students Registration uchun API hujjati",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Planetconsulting/', include('education.urls')),
]
