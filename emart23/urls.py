from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Define Rest Framework Router
router = DefaultRouter()

""" Authentication URL Patterns """

AUTHENTICATION_URL_PATTERNS = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

""" Third Party packages URL Patterns """

THIRD_PARTY_PACKAGES_URL_PATTERNS = [
    # packages
]

""" Internal Application URL Patterns """

INTERNAL_APP_URL_PATTERNS = [
    # Apps
]

# Root URL Patterns

urlpatterns = [
    path('admin/', admin.site.urls),
] + AUTHENTICATION_URL_PATTERNS + THIRD_PARTY_PACKAGES_URL_PATTERNS + INTERNAL_APP_URL_PATTERNS
