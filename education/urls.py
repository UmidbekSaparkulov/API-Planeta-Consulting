from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, ProgramViewSet, StudentsRegistrationViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename='countries')
router.register(r'programs', ProgramViewSet, basename='programs')
router.register(r'students', StudentsRegistrationViewSet, basename='students')

urlpatterns = [
    path('api/', include(router.urls)),
]
