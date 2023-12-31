from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from social.models import User
from bookcollections.models import CollectionDAO


# Create your views here.
@login_required
def index(request):
    context = {
        'collections':  CollectionDAO.get_all_by_user(request.user.id)
    }
    return render(request, 'index.html', context=context)


def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']

        # Verifica si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe. Por favor, elige otro.')
            return render(request, 'registration/register.html')

        if user_type == 'professor':
            User.objects.create_professor_user(
                username=username,
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname)
        elif user_type == 'reader':
            User.objects.create_reader_user(
                username=username,
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname
            )
        else:
            return render(request, 'registration/register.html')

        login(request, User.objects.get(username=username))
        return redirect('/')

    return render(request, 'registration/register.html')
