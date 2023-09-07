from django.http import HttpResponse, FileResponse
from django.shortcuts import render


# Create your views here.

def serve_document(request, file_path: str):
    return FileResponse(open(f"articles/{file_path}", 'rb'))
