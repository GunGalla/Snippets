from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Snippet


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'pages/view_snippets.html', context)


def snippet(request, id):
    try:
        dist_snippet = Snippet.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Snippet, with id={id} not found :(")
    context = {'snippet': dist_snippet}
    return render(request, 'pages/snippet.html', context)
