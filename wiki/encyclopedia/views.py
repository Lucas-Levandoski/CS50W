from django import forms
from django.shortcuts import render
from django.urls import is_valid_path
from . import util


class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wikiPage(request, title):
    entry = util.get_entry(title)

    if entry == None:
        return render(request, "encyclopedia/not-found.html", {
            "title": "Not Found"
        })

    return render(request, "encyclopedia/wiki-page.html", {
        "title": title,
        "entry": entry,
    })


def newPage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            util.save_entry(
                form.cleaned_data["title"],
                form.cleaned_data["content"]
            )

    return render(request, "encyclopedia/new-page.html", {
        "form": NewPageForm()
    })


def editPage(request):
    return render(request, "encyclopedia/new-page.html")
