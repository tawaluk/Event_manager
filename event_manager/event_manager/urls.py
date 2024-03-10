from django.contrib import admin
from django.urls import path
from backend.views import EventListView
from users.views import MyTokenObtainPairView, RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('events/', EventListView.as_view(), name='event-list'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

