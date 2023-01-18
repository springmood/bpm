from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserDetailAPI,RegisterUserAPIView,MyObtainTokenPairView


urlpatterns=[
    # path("get-details",UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
    path('login', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]