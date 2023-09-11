from django.shortcuts import render, redirect
from bookcollections.models import Collection, CollectionDAO
from articles.models import Document, Category
from django.contrib.auth.decorators import login_required


@login_required
def view_collections(request):
    # create_base_data(request, is_set)
    collections = []
    external_collections = []
    search = request.GET.get("search", "")
    tipo = request.GET.get("tipo", "")
    privacidad = request.GET.get("privacy", "all")

    if search and tipo:

        if tipo == "name":
            collections = CollectionDAO.search_by_name_and_user(search, request.user.id)
            external_collections = Collection.objects.filter(name__icontains=search).exclude(user_id=request.user.id)
        elif tipo == "category":
            collections = CollectionDAO.search_by_category_and_user(search, request.user.id)
            external_collections = Collection.objects.filter(category__icontains=search).exclude(user_id=request.user.id)
    else:
        collections = CollectionDAO.get_all_by_user(request.user.id)
        external_collections = Collection.objects.all().exclude(user_id=request.user.id)

    if privacidad == "public":
        collections = collections.filter(is_public=True)
        external_collections = external_collections.filter(is_public=True)[:10]
    elif privacidad == "private":
        collections = collections.filter(is_public=False)
        external_collections = external_collections.filter(is_public=False)[:10]

    context = {
        'collections': collections,
        'search': search,
        'external_collections': external_collections
    }

    return render(request, './collections/collections.html', context=context)


@login_required
def view_singe_collection(request, id):
    collection = CollectionDAO.get_collection(id)
    print(collection.user.followers)
    return render(request, 'collections/collection.html', context={'collection': collection})


@login_required
def add_book(request, collection_id):
    collection = Collection.objects.filter(user_id=request.user.id, id=collection_id).first()
    if request.POST:
        for i in request.POST.getlist("selected_books"):
            CollectionDAO.add_book(collection, Document.objects.get(uid=i))
        return redirect(f'/collections/{collection_id}')

    context = {
        'books': Document.objects.filter(category=collection.category),
        'collection': collection
    }
    return render(request, 'collections/add_book.html', context=context)


@login_required
def create_coll(request):
    context = {}
    context["categories"] = [c[0] for c in Category.choices ]
    category = request.GET.get("category")
    first = request.GET.get("first")
    if first:
        context["books"] = Document.objects.filter(category=category)
        context["category"] = category

    if request.POST:
        selected_books_ids = request.POST.getlist("selected_books")
        selected_books = []
        col = CollectionDAO.create(
            name=request.POST.get("name"),
            description=request.POST.get("desc"),
            is_public=request.POST.get("public") == "on",
            category=request.POST.get("category"),
            user_ref=request.user.id
        )

        for i in selected_books_ids:
            CollectionDAO.add_book(col, Document.objects.get(uid=i))
        return redirect('/collections')

    return render(request, 'collections/create.html', context=context)

"""
    if request.GET:

        book_id = request.GET.get("doc_id", "")
        category = request.GET.get("category", "")
        book = None
        if book_id:
            book_id = int(book_id)
            book = Document.objects.filter(uid=book_id).first()
            context['doc'] = book
            context['categories'] = Category.choices

        return render(request, './collections/create.html', context)

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
            category=category,
            user_ref=request.user.id,
            book_ref=int(book)
        )

        return redirect('/collections')
    return render(request, './collections/create.html')
"""