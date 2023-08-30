from django.shortcuts import render
from bookcollections.models import CollectionDAO
from django.http import HttpResponse



#return base.html
def view_base(request):
   return render(request, './base.html')

#return collections.html
def view_collections(request):
      return render(request, './collections.html')

#create collections data for test 

collections = [
   {
      'id': 1,
      'name': 'collection1',
      'description': 'description1',
      'categories': ['Categoría A', 'Categoría B'],
      'books': [
            {
               'title': 'Libro 1',
               'author': 'Autor 1',
               
            },
            {
               'title': 'Libro 2',
               'author': 'Autor 2',
            },
         ]
   },
   {
      'id': 2,
      'name': 'collection2',
      'description': 'description2',
      'categories': ['Categoría C', 'Categoría D'],
      'books': [
         {
               'title': 'Libro 1',
               'author': 'Autor 1',
               
            },
      ]
   },
   {
      'id': 3,
      'name': 'collection3',
      'description': 'description3',
      'categories': ['Categoría F', 'Categoría E'],
      'books': [
         {
               'title': 'Libro 1',
               'author': 'Autor 1',
            },
         {
               'title': 'Libro 7',
               'author': 'Autor 7',
            },
         {
               'title': 'Libro 5',
               'author': 'Autor 5',
            },
      ]
   },
]

