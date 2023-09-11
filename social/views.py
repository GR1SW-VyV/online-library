from django.shortcuts import render, redirect
from .models import User
from bookcollections.models import Collection, CollectionDAO
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def profile(request, user_username):
    user_profile = User.objects.get(username=user_username)
    collections = CollectionDAO.get_all_by_user(user_profile.id).filter(is_public=True)
    is_own_profile = request.user.is_authenticated and request.user == user_profile
    already_following = request.user.is_authenticated and user_profile.is_followed_by(request.user)
    return render(request, 'social/profile.html', {
        'user_profile': user_profile,
        'is_own_profile': is_own_profile,
        'already_following': already_following,
        'collections': collections
    })


@login_required
def feed(request):
    user_profile = request.user
    feed_items = user_profile.feed.all().order_by('-date', '-time')
    return render(request, 'social/feed.html', {
        'feed': feed_items
    })


@login_required
def follow_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    user_profile = request.user

    if not collection.is_followed_by(user_profile):
        user_profile.follow(collection)

    return redirect('collections', user_id=request.user.id)


@login_required
def follow_reader(request, user_username):
    reader_to_follow = User.objects.get(username=user_username)
    user_profile = request.user

    if reader_to_follow.id == user_profile.id or reader_to_follow.is_followed_by(user_profile):
        return redirect('profile', user_username=user_username)

    user_profile.follow(reader_to_follow)
    return redirect('profile', user_username=user_username)


def search_users(request):
    q = request.GET.get('q', '')
    users = User.objects.filter(
        Q(username__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q)
    ).order_by('-followers').distinct()
    return render(request, 'social/users.html', {
        'users': users,
        'q': q
    })
