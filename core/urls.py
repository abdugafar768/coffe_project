from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/', include('api.urls')),
]