from api.views import CustomTokenObtainPairView
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path(
        'api/auth/token/login/',
        CustomTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
]
