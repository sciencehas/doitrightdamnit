```python
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Document
from .utils.file_handler import handle_uploaded_file
from .utils.document_processor import process_document
from .utils.similarity_analyzer import analyze_similarity

def index(request):
    documents = Document.objects.all()
    return render(request, 'app/index.html', {'documents': documents})

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('index')
    else:
        form = UploadForm()
    return render(request, 'app/upload.html', {'form': form})

def process(request, document_id):
    document = Document.objects.get(id=document_id)
    processed_document = process_document(document)
    return render(request, 'app/result.html', {'document': processed_document})

def analyze(request, document_id):
    document = Document.objects.get(id=document_id)
    similarity_results = analyze_similarity(document)
    return render(request, 'app/detail.html', {'results': similarity_results})
```