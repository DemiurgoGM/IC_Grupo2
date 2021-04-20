from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    context = {
        'title': 'HomePage',
    }
    return render(request, 'IC_Grupo2_App/home.html', context)


def send(request):
    if request.method == 'GET':
        return redirect('IC_Grupo2_HomePage')

    enderecos_untreated = request.POST.get('enderecos')
    enderecos_list = enderecos_untreated.split(';')
    enderecos_list = [x.strip() for x in enderecos_list if x]
    print(enderecos_list)
    for file in request.FILES['files']:
        # TODO usar file recebido
        pass

    # Como responder com um csv:
    # response = HttpResponse(file, headers={
    #     'Content-Type': 'text/csv',
    #     'Content-Disposition': 'attachment; filename="foo.csv"',
    # })

    # Como responder com um zip:
    # response = HttpResponse(file, headers={
    #     'Content-Type': 'application/zip',
    #     'Content-Disposition': 'attachment; filename="foo.zip"',
    # })

    file = None
    response = HttpResponse(file, headers={
        'Content-Type': 'application / vnd.openxmlformats - officedocument.presentationml.presentation',
        'Content-Disposition': 'attachment; filename="foo.pptx"',
    })
    return response
