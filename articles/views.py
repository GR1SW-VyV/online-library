import hashlib
import os
import random
import time

from django.http import HttpResponse, FileResponse,HttpRequest
from django.shortcuts import render,redirect
from django.template.backends import django
from django.views.decorators.csrf import csrf_exempt

from articles.models import Document


# Create your views here.

def serve_document(request, file_path: str):
    return FileResponse(open(f"{file_path}", 'rb'))

@csrf_exempt
def show_upload_document_form(request:HttpRequest):
    if(request.method == "GET"):
        return FileResponse(open(f"templates/upload/subirArticulo.html", 'rb'))

    title = request.POST["title"]
    category = request.POST["materia-tematica"]
    type = request.POST["tipo"]
    author = request.POST["author"]

    filename:str = str(request.FILES["file"])
    rnd_dir = hashlib.md5(random.randbytes(128)).hexdigest()
    rnd_path = os.path.join(rnd_dir,filename)
    tmp_path = os.path.join("tmp", rnd_path)
    os.mkdir(os.path.dirname(tmp_path))

    with open(tmp_path,"wb+") as f:
        for c in request.FILES["file"].chunks():
            f.write(c)

    doc:Document = Document.from_local_path(
        tmp_path,
        title = title,
        category = category,
        type = type,
        author = author
    )


    return redirect(f"/articles/document/{doc.uid}")

def show_document(request:HttpRequest, document_id):
    doc:Document = Document.objects.get(uid=document_id)

    return render(request, "social/../templates/upload/visualizarInformacion.html", {
        "document":doc
    })

def score_document(request:HttpRequest, document_id, score):
    doc:Document = Document.objects.get(uid=document_id)
    current_user = request.user
    if not request.user.is_authenticated:
        return HttpResponse(status=403)

    doc.add_score(current_user.id,score)

    return HttpResponse(doc.score(),status=200)