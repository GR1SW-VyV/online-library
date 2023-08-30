from django.shortcuts import render
from bookcollections.models import CollectionDAO
from django.http import HttpResponse



#return collections.html
def view_collections(request):
      return render(request, './collections.html', context={'collections': collections})

#create collections data for test 

collections = [
   {
      'id': 1,
      'name': 'collection1',
      'cover':'https://i.pinimg.com/564x/91/83/7d/91837dd303b431b003d9d9e76ea91d30.jpg',
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
      'cover':'https://i.pinimg.com/564x/d1/a5/cc/d1a5cc99e240591db113023438329fce.jpg',
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
      'cover':'https://i.pinimg.com/564x/a6/46/b2/a646b21d519edd807e7817e14c28af07.jpg',
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
      ]
   },
]

