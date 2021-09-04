from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.



def show(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['files']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        return render(request, 'form.html')
    return render(request, 'index.html')
