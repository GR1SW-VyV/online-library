import os
import hashlib
import shutil

from articles.models import Document
from ..choices.category import Category


def from_local_path(path:str, /, author="", title="", category=Category.UNKNOWN, **kwargs) -> Document:
    categoryStr = str(category).capitalize()
    os.makedirs(f'./articles/resources/{categoryStr}Resources', exist_ok=True)
    shutil.copy(path, f'./articles/resources/{categoryStr}Resources/')

    file = open(path, "rb")
    sha512 = hashlib.sha512(file.read()).hexdigest()

    print(kwargs)

    filename = path.split("/")[-1]

    return Document(filename=filename, sha512=sha512, **kwargs)
