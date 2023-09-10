from django.shortcuts import render, redirect
from .models import User, Collection
from django.contrib.auth.decorators import login_required


def profile(request, user_id):
    user_profile = User.objects.get(id=user_id)
    is_own_profile = request.user.is_authenticated and request.user == user_profile
    already_following = request.user.is_authenticated and user_profile.is_followed_by(request.user)
    return render(request, 'social/profile.html', {
        'user_profile': user_profile,
        'is_own_profile': is_own_profile,
        'already_following': already_following
    })


@login_required
def feed(request):
    user_profile = request.user
    return render(request, 'social/feed.html', {'user_profile': user_profile})


@login_required
def follow_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    user_profile = request.user

    if not collection.is_followed_by(user_profile):
        user_profile.follow(collection)

    return redirect('collections', user_id=request.user.id)


@login_required
def follow_reader(request, user_id):
    reader_to_follow = User.objects.get(id=user_id)
    user_profile = request.user

    if reader_to_follow.id == user_profile.id:
        return redirect('profile', user_id=user_id)

    if reader_to_follow.is_followed_by(user_profile):
        return redirect('profile', user_id=user_id)

    user_profile.follow(reader_to_follow)
    return redirect('profile', user_id=user_id)
