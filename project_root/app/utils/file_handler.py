```python
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

def handle_uploaded_file(upload_file):
    path = default_storage.save('tmp/' + upload_file.name, ContentFile(upload_file.read()))
    return os.path.join(settings.MEDIA_ROOT, path)

def handle_uploaded_files(files):
    file_paths = []
    for file in files:
        path = handle_uploaded_file(file)
        file_paths.append(path)
    return file_paths

def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
    else:
        raise ValueError("File not found in the specified path.")
```