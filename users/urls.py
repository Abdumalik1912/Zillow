from django.urls import path
from users.views import Login, Logout, Register, CustomUserUpdate, Profile, ProfileUpdate

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('update_user', CustomUserUpdate.as_view(), name='update_user'),
    path('profile', Profile.as_view(), name='profile'),
    path('update_profile', ProfileUpdate.as_view(), name='update_profile'),
]
