from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

from weasyprint import HTML


def generate_pdf(request):

    html_string = render_to_string('invoice.html')
    html = HTML(string=html_string)
    pdf = html.write_pdf('invoice.pdf')

    context = {}
    return render(request, 'invoice.html', context)
