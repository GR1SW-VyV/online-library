import hashlib
import os
import random
import time

from django.http import HttpResponse, FileResponse,HttpRequest
from django.shortcuts import render
from django.template.backends import django
from django.views.decorators.csrf import csrf_exempt

from articles.models import Document


# Create your views here.

def serve_document(request, file_path: str):
    return FileResponse(open(f"articles{file_path}", 'rb'))

@csrf_exempt
def show_upload_document(request:HttpRequest):
    if(request.method == "GET"):
        return FileResponse(open(f"templates/social/subirArticulo.html", 'rb'))

    title = request.POST["title"]
    category = request.POST["materia-tematica"]
    type = request.POST["tipo"]
    filename:str = str(request.FILES["file"])
    rnd_dir = hashlib.md5(random.randbytes(128)).hexdigest()
    rnd_path = os.path.join(rnd_dir,filename)
    tmp_path = os.path.join("tmp", rnd_path)
    os.mkdir(os.path.dirname(tmp_path))

    with open(tmp_path,"wb+") as f:
        for c in request.FILES["file"].chunks():
            f.write(c)

    Document.from_local_path(
        tmp_path,
        title = title,
        category = category,
        type = type
    )

    print(request.FILES["file"])

    return HttpResponse("<h1>Yes</h1>")
