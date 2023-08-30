from django.shortcuts import render

# Create your views here.


def view(request):
    return render(request, './templates/base.html')
