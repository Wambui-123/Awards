from django.shortcuts import render, redirect, get_object_or_404
from awards_app.forms import SignupForm, ChangePasswordForm, EditProfileForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from awards_app.models import Profile
from post.models import Post, Follow, Stream
from django.db import transaction
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, resolve

from django.core.paginator import Paginator

# Create your views here.
def Signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			User.objects.create_user(username=username, email=email, password=password)
			return redirect (reverse("index"))
	else:
		form = SignupForm()
	
	context = {
		'form':form,
	}

	return render(request, 'signup.html', context)

def UserProfile(request, username):
	user = get_object_or_404(User, username=username)
	profile = Profile.objects.get(user=user)
	url_name = resolve(request.path).url_name
 
	if url_name == 'profile':
			posts = Post.objects.filter(user=user).order_by('-posted')
	else: 
			posts = profile.favorites.all()

	# Pagination
	paginator = Paginator(posts, 8)
	page_number = request.GET.get('page')
	post_paginator = paginator.get_page(page_number)

	template = loader.get_template('profile.html')

	context = {
		'posts': post_paginator,
		'profile':profile,
		'url_name': url_name
	}

	return HttpResponse(template.render(context, request))

@login_required
def EditProfile(request):
	user = request.user.id
	profile = Profile.objects.get(user__id=user)

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile.picture = form.cleaned_data.get('picture')
			profile.first_name = form.cleaned_data.get('first_name')
			profile.last_name = form.cleaned_data.get('last_name')
			profile.location = form.cleaned_data.get('location')
			profile.url = form.cleaned_data.get('url')
			profile.profile_info = form.cleaned_data.get('profile_info')
			profile.save()
			return redirect('index')
	else:
		form = EditProfileForm()

	context = {
		'form':form,
	}

	return render(request, 'edit_profile.html', context)
