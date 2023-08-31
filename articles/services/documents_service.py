import os
import hashlib
import shutil

from articles.models import Document



def from_local_path(path:str, /, author="", title="", category=Document.Category.UNKNOWN, **kwargs) -> Document:
    categoryStr = str(category).capitalize()
    os.makedirs(f'./articles/resources/{categoryStr}Resources', exist_ok=True)
    shutil.copy(path, f'./articles/resources/{categoryStr}Resources/')

    file = open(path, "rb")
    sha512 = hashlib.sha512(file.readlines())

    print(kwargs)

    filename = path.split("/")[-1]

    author_prefix = author[0:2]
    title_prefix = title[0:2]
    category_prefix = str(category).capitalize()

    kwargs["uid"] = "".join([title_prefix, author_prefix, category_prefix])
    return Document(filename=filename, sha512=sha512, **kwargs)
