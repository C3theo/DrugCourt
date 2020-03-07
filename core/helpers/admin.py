import os
import shutil
from pathlib import Path

from django.conf import settings

def delete_all_migrations():
    """
        Delete migrations from all Apps.
    """
    base_path = Path(settings.BASE_DIR)
    migration_files = [each for each in base_path.glob(
        '../*/migrations/[!__init__]*.py')]

    for f in migration_files:
        os.unlink(f)

