import os
import shutil

from articles.models import Article


def from_local_path(path, author="", title="", **kwargs) -> Article:
    os.makedirs(f'./articles/resources/{kwargs["subject"]}Resources', exist_ok=True)
    shutil.copy(path, f'./articles/resources/{kwargs["subject"]}Resources/')

    print(kwargs)

    author_prefix = author[0:2]
    title_prefix = title[0:2]
    subject_prefix = kwargs["subject"]

    kwargs["uid"] = "".join([author_prefix, title_prefix, subject_prefix])
    return Article(**kwargs)
