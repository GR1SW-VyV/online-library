from django.shortcuts import render


def view_recommendations(request):
    return render(request, './recommendation/recommended.html', context={'recommendations': recommendations})


def view_form_preferences(request):
    return render(request, './recommendation/form_preferences.html', context={'recommendations': recommendations})


# create collections data for test
recommendations = [
    {
        'category': 'Matemática',
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
        ]
    }
]
