import tempfile

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {'offline': False})


def home_offline(request):
    return render(request, 'home.html', {'offline': True})


def details(request, template):
    return render(request, f'{template}.html', {'offline': False})


def download(request):
    # `pip install django-weasyprint==1.0.2`
    # `brew install pango@1.48.0`
    # Add 'weasyprint' to INSTALLED_APPS (in settings.py)
    from weasyprint import HTML

    rendered = render_to_string('home.html', {'offline': True})
    html = HTML(string=rendered, base_url=request.build_absolute_uri())
    result = html.write_pdf(presentational_hints=True, zoom=1)

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=cv.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response
