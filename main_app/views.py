from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, PostForm
from .models import Profile, Post

# Create your views here.
def home(request):
  return render(request, 'home.html')

# REGISTRATION & PROFILE RELATED VIEWS
def profile(request):
  print(request)
  profile = Profile.objects.get(user = request.user)
  posts = Post.objects.filter(user = request.user)
  context = {'profile': profile, 'posts': posts}
  return render(request, 'profile/home.html', context)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      print('USER------------------->', user)
      login(request, user)
      return redirect('new_profile')
    else:
      error_message = 'Invalid sign up - please try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def new_profile(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    if form.is_valid():
      new_profile = form.save(commit=False)
      new_profile.user = request.user
      new_profile.save()
      print('NEW_PROFILE---------------------------->', new_profile)
      return redirect('profile_home', new_profile.id)
    else:
      return render(request, 'profile/new.html', {'form': form})
  else: 
    form = ProfileForm()
    context = {'form': form}
    return render(request, 'profile/new.html', context)

def profile_home(request, profile_id):
  print('REQUEST--------------------------------->', profile_id)
  profile = Profile.objects.get(user = profile_id)
  posts = Post.objects.filter(user = profile_id)
  print('POSTS LOG-------------------------------------->', posts)
  context = {'profile': profile, 'posts': posts}
  return render(request, 'profile/home.html', context)

def edit_profile(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  if request.user == profile.user:
      if request.method == 'POST':
          form = ProfileForm(request.POST, instance=profile)
          if form.is_valid():
              updated_profile = form.save()
              return redirect('profile_home', updated_profile.id)
      else:
          form = ProfileForm(instance=profile)
          context = {'form': form}
          return render(request, 'profile/edit.html', context)
  else: 
      raise PermissionDenied("You can't edit another user's profile!")

# POST RELATED VIEWS
def posts(request):
  posts = Post.objects.all()
  context = {'posts': posts}
  return render(request, 'post/index.html', context)

def create_post(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      new_post = post_form.save(commit=False)
      new_post.user = request.user
      new_post.save()
      return redirect('posts')
  else:
    form = PostForm()
    context = {'form': form}
    return render(request, 'post/new.html', context)

def post_details(request, post_id):
  post = Post.objects.get(id=post_id)
  context = {'post': post}
  return render(request, 'post/show.html', context)

def delete_post(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.user == post.user:
    post.delete()
    return redirect('posts')
  else:
    raise PermissionDenied("You can't delete someone else's post!")

def edit_post(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.user == post.user:
    if request.method == 'POST':
      post_form = PostForm(request.POST, instance=post)
      if post_form.is_valid():
        updated_post = post_form.save()
        return redirect('post_details', updated_post.id)
    else:
      form = PostForm(instance=post)
      context = {'form': form}
      return render(request, 'post/edit.html', context)
  else:
    raise PermissionDenied("You can't edit someone else's post!")