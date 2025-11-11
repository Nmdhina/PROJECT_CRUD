from django.urls import path, include
from .views import LoginView, logoutView, RegisterView, StudentsViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentsViewset, basename='students')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]
