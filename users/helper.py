from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def save_file(request, file):
    if file is None:
        return None 
    file_name = file.name
    file_path = default_storage.save(f"static/images/{file_name}",ContentFile(file.read()))
    Url = request.build_absolute_uri(default_storage.url(file_path))
    return Url