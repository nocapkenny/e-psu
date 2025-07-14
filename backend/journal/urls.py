from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('userapp.urls')),
    path('api/school/', include('schooltable.urls')),
    path('api/table/', include('mark.urls')),
    path('api/login/', TokenObtainPairView.as_view())
]
