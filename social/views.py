from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User, Collection, Activity
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def hello(request):
    # TODO implement login
    user = authenticate(request, username="test", password="test")
    if user is not None:
        login(request, user)
    return HttpResponse("Hello World")


def profile(request, user_id):
    user_profile = User.objects.get(id=user_id)
    is_own_profile = request.user.is_authenticated and request.user == user_profile
    return render(request, 'social/profile.html', {'user_profile': user_profile, 'is_own_profile': is_own_profile})


@login_required
def feed(request):
    user_profile = User.objects.get(id=request.user.id)
    return render(request, 'social/feed.html', {'user_profile': user_profile})


@login_required
def follow_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    user_profile = User.objects.get(id=request.user.id)
    user_profile.follow(collection)
    return redirect('collections', user_id=request.user.id)


@login_required
def follow_reader(request, user_id):
    reader_to_follow = User.objects.get(id=user_id)
    user_profile = User.objects.get(id=request.user.id)

    if reader_to_follow.id == user_profile.id:
        return redirect('profile', user_id=user_id)

    user_profile.follow(reader_to_follow)
    return redirect('profile', user_id=user_id)
