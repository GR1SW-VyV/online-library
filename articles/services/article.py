import os
import shutil

from articles.models import Article


def from_local_path(path, /, author="", title="", category=Article.Category.UNKNOWN, **kwargs) -> Article:
    categoryStr = str(category).capitalize()
    os.makedirs(f'./articles/resources/{categoryStr}Resources', exist_ok=True)
    shutil.copy(path, f'./articles/resources/{categoryStr}Resources/')

    print(kwargs)

    author_prefix = author[0:2]
    title_prefix = title[0:2]
    category_prefix = str(category).capitalize()

    kwargs["uid"] = "".join([author_prefix, title_prefix, category_prefix])
    return Article(**kwargs)
