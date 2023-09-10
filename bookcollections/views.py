from django.shortcuts import render, redirect
from bookcollections.models import Collection, CollectionDAO
from articles.models import Document, Category
import faker
from django.http import HttpResponse

is_set = False


# return collections.html

# create collections data for test
def create_base_data(request, is_set):
    def create_col(user):
        fake = faker.Faker()
        col = CollectionDAO.create(
            name=fake.name(),
            description=fake.text(),
            category=Category.UNKNOWN,
            is_public=True,
            user_ref=request.user.id
        )

        for i in range(0, 10):
            doc = Document.objects.create(title=fake.name())
            CollectionDAO.add_book(col, doc)

        return col

    if not is_set:
        is_set = True
        for i in range(0, 5):
            create_col(request.user.id)


def view_collections(request):
    # create_base_data(request, is_set)
    collections = []
    search = request.GET.get("search", "")
    tipo = request.GET.get("tipo", "")
    privacidad = request.GET.get("privacy", "all")

    if search and tipo:

        if tipo == "name":
            collections = CollectionDAO.search_by_name_and_user(search, request.user.id)
        elif tipo == "category":
            collections = CollectionDAO.search_by_category_and_user(search, request.user.id)
    else:
        collections = CollectionDAO.get_all_by_user(request.user.id)

    if privacidad == "public":
        collections = collections.filter(is_public=True)
    elif privacidad == "private":
        collections = collections.filter(is_public=False)

    return render(request, './collections/collections.html', context={'collections': collections, 'search': search})


def view_singe_collection(request, id):
    collection = CollectionDAO.get_collection(id)
    return render(request, 'collections/collection.html', context={'collection': collection})


def create_coll(request):
    if request.GET:

        book_id = request.GET.get("doc_id", "")
        book = None
        if book_id:
            book_id = int(book_id)
            book = Document.objects.filter(uid=book_id).first()
        return render(request, './collections/create.html', {'doc': book})

    elif request.POST:
        name = request.POST["name"]
        desc = request.POST["description"]
        is_public = request.POST.get("is_public", "") == "on"
        category = request.POST["category"]
        book = request.POST["doc_id"]

        CollectionDAO.create_with_book(
            name=name,
            description=desc,
            is_public=is_public,
            category=Category.UNKNOWN,
            user_ref=request.user.id,
            book_ref=int(book)
        )

        return redirect('/collections')
    return render(request, './collections/create.html')
