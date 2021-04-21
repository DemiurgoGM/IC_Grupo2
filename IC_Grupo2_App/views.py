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
    enderecos_list = None
    if enderecos_untreated:
        enderecos_list = enderecos_untreated.split(';')
        enderecos_list = [x.strip() for x in enderecos_list if x and x.strip()]
    if not enderecos_list:
        # TODO sem endereco
        pass
    for file in request.FILES['files']:
        # TODO usar file(s) (podem ser múltiplos) recebido(s)
        pass

    # Testes para envio:

    # Como responder com um csv: - Sem teste
    # response = HttpResponse(file, headers={
    #     'Content-Type': 'text/csv',
    #     'Content-Disposition': 'attachment; filename="foo.csv"',
    # })

    # Como responder com um zip: - Sem teste
    # response = HttpResponse(file, headers={
    #     'Content-Type': 'application/zip',
    #     'Content-Disposition': 'attachment; filename="foo.zip"',
    # })

    # Como responder com um pdf: - Funcional
    file = request.FILES['files']
    response = HttpResponse(file, headers={
        'Content-Type': 'application/pdf',
        'Content-Disposition': 'attachment; filename="foo.pdf"',
    })

    return response
