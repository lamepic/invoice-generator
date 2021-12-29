from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

# from weasyprint import HTML


def generate_pdf(request):

    context = {}
    return render(request, 'invoice.html', context)
