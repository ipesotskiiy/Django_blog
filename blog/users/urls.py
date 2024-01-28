from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import (
    RegisterUserAPIView,
    MyTokenObtainPairView,
    UserViewSet,
    UserFollowingViewSet
)

app_name = 'users'

urlpatterns = [
    path('auth/signin', MyTokenObtainPairView.as_view(), name='signin'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/signup', RegisterUserAPIView.as_view(), name='signup'),
    path('user/all', UserViewSet.as_view({'get': 'list'})),
    path('follower/add/<pk>', UserFollowingViewSet.as_view({'post': 'create'})),
    path('follower/delete/<pk>', UserFollowingViewSet.as_view({'delete': 'destroy'})),
]
