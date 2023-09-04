import shutil
from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.TextChoices):
    UNKNOWN = "UNKNOWN", _('UNKNOWN')
    MATH = "MATH", _('MATH')
    PHYSICS = "PHYSICS", _('PHYSICS')
    CALCULUS = "CALCULUS", _('CALCULUS')
    PROGRAMMING = "PROGRAMMING", _('PROGRAMMING')
    LITERATURE = "LITERATURE", _('LITERATURE')
    ECONOMY = "ECONOMY", _('ECONOMY')
    GEOMETRY = "GEOMETRY", _('GEOMETRY')
    CHEMISTRY = "CHEMISTRY", _('CHEMISTRY')