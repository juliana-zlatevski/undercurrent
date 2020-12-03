from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # REGISTRATION + ACCOUNT RELATED ROUTES
  path('accounts/signup', views.signup, name='signup'),
  path('profile/new', views.new_profile, name='new_profile'),
  path('profile', views.profile, name='profile'),
  path('accounts/profile/<int:profile_id>/', views.profile_home, name='profile_home'),
  path('profile/<int:profile_id>/edit', views.edit_profile, name='edit_profile'),
  # POST RELATED ROUTES
  path('posts/', views.posts, name='posts'),
  path('posts/create', views.create_post, name='create_post'),
  path('post/<int:post_id>/', views.post_details, name='post_details'),
  path('post/<int:post_id>/delete_post', views.delete_post, name='delete_post'),
  path('post/<int:post_id>/edit', views.edit_post, name='edit_post')
]

