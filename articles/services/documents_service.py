import os
import hashlib
import shutil

from articles.models import Document
from ..choices.category import Category


def from_local_path(path: str, /, author="", title="", category=Category.UNKNOWN, **kwargs) -> Document:
    category_str = str(category).capitalize()
    os.makedirs(f'./articles/resources/{category_str}Resources', exist_ok=True)
    shutil.copy(path, f'./articles/resources/{category_str}Resources/')

    file = open(path, "rb")
    sha512 = hashlib.sha512(file.read()).hexdigest()
    filename = path.split("/")[-1]

    return Document(filename=filename, sha512=sha512, **kwargs)
