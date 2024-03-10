from django.contrib import admin
from django.urls import path, include
from users.views import MyTokenObtainPairView, RegisterView, LoginView

from rest_framework.routers import DefaultRouter
from backend.views import OrganizationViewSet, EventViewSet


router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'events', EventViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
]

