import os
import shutil

from articles.models import Article


def from_local_path(path, **kwargs) -> Article:
    os.makedirs(f'./articles/resources/{kwargs["subject"]}Resources', exist_ok=True)
    shutil.copy(path, f'./articles/resources/{kwargs["subject"]}Resources/')
    return Article(**kwargs)
