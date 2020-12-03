from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # registration/accounts
  path('accounts/signup', views.signup, name='signup'),
  path('profile/new', views.new_profile, name='new_profile'),
  path('profile/<int:profile_id>/', views.profile_home, name='profile_home'),
]