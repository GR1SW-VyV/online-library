from django.shortcuts import render


# Create your views here.
def mynotes(request):
    return render(request, '../templates/annotations/my-notes.html')
