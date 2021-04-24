from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

import os

from .modules.sad.factory import ApplicationFactory

def home(request):
    context = {
        'title': 'HomePage',
    }
    return render(request, 'IC_Grupo2_App/home.html', context)


def send(request):
    if request.method == 'GET':
        return redirect('IC_Grupo2_HomePage')

    endereco = request.POST.get('endereco')
    input_file = request.FILES['file']
    
    path = default_storage.save('tmp/input_file.pdf', ContentFile(input_file.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
 
    highlighted_pdf, csv = ApplicationFactory().get_application_instance(tmp_file, endereco).run()

    # response = HttpResponse(file, headers={
    #     'Content-Type': 'application/zip',
    #     'Content-Disposition': 'attachment; filename="foo.zip"',
    # })

    return response