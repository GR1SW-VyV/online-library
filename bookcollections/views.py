from django.shortcuts import render
from bookcollections.models import CollectionDAO
from django.http import HttpResponse



#return base.html
def view_base(request):
   return render(request, './base.html')

#return collections.html
def view_collections(request):
      return render(request, './collections.html')

