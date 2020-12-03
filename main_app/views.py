from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
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
          return redirect('profile_home', new_profile.id)
      else:
          return render(request, 'profile/new.html', {'form': form})
  else: 
        form = ProfileForm()
        context = {'form': form}
        return render(request, 'profile/new.html', context)

def profile_home(request, profile_id):
  profile = Profile.objects.get(user = request.user)
  posts = Post.objects.filter(user = request.user)
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