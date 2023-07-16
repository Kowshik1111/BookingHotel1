from django.urls import path
from users.views import login_view, logout_view, create_user

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create-user/', create_user, name='create_user'),
]
