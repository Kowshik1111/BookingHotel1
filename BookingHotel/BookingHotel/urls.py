from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('hotel_management_admin/', include('hotel_management_admin.urls')),
    path('', include('home.urls')),
]
