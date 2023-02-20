from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Snippet
from .forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета', 'form': form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippet_list')


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
