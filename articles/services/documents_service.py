import os
import hashlib
import shutil

from articles.models import Document
from ..choices.category import Category

from_local_path = Document.from_local_path
