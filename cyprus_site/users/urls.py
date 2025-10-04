from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('profile/update/', views.ProfileUpdate.as_view(), name='update_profile'),
    path('profile/delete/', views.ProfileDelete.as_view(), name='delete_profile'),
]
