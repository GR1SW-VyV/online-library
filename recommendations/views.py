from django.shortcuts import render


def view_recommendations(request):
    return render(request, './recommendation/recommended.html', context={'recommendations': recommendations})


def view_form_preferences(request):
    return render(request, './recommendation/form_preferences.html', context={'recommendations': recommendations})


# create recommendation data for test
recommendations = [
    {
        'category': 'Matemática',
        'books': [
            {
                'title': 'Libro 1',
                'author': 'Autor 1',
                'document_id': '1'
            },
            {
                'title': 'Libro 2',
                'author': 'Autor 2',
                'document_id': '1'
            },
{
                'title': 'Libro 8',
                'author': 'Autor 8',
                'document_id': '1'
            },
{
                'title': 'Libro 9',
                'author': 'Autor 9',
                'document_id': '12345'
            }
        ]
    },
    {
        'category': 'Física',
        'books': [
            {
                'title': 'Libro 3',
                'author': 'Autor 3',
            },
            {
                'title': 'Libro 4',
                'author': 'Autor 4',
            },
{
                'title': 'Libro 10',
                'author': 'Autor 10',
            },
{
                'title': 'Libro 11',
                'author': 'Autor 11',
            },
        ]
    },
    {
        'category': 'Programación',
        'books': [
            {
                'title': 'Libro 5',
                'author': 'Autor 5',
            },
            {
                'title': 'Libro 6',
                'author': 'Autor 6',
            },
{
                'title': 'Libro 12',
                'author': 'Autor 12',
            },
{
                'title': 'Libro 13',
                'author': 'Autor 13',
            },
        ]
    }
]
