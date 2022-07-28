from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util


class PageForm(forms.Form):
    title = forms.CharField(label="Title", required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)


def index(request):
    title = request.GET.get("title")
    pageMD = util.get_entry(title)

    if pageMD is not None:
        return HttpResponseRedirect(
            reverse("wikiPage", args=[title])
        )

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
        form = PageForm(request.POST)

        form.is_valid()

        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]

        if form.is_valid() and util.get_entry(title) is None:
            util.save_entry(
                title,
                content
            )
            return HttpResponseRedirect(
                reverse("wikiPage", args=[title])
            )
        else:
            if util.get_entry(title) is not None:
                form.add_error("title", "this title already exists")

            return render(request, "encyclopedia/new-page.html", {
                "form": form
            })

    return render(request, "encyclopedia/new-page.html", {
        "form": PageForm()
    })


def editPage(request):
    if request.method == "POST":
        form = PageForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            util.save_entry(title, content)

            return HttpResponseRedirect(
                reverse("wikiPage", args=[title])
            )

        return render(request, "encyclopedia/edit-page.html", {
            "form": form
        })

    title = request.GET.get("title")
    data = {
        "title": title,
        "content": util.get_entry(title)
    }

    form = PageForm(data)

    if form.is_valid():
        return render(request, "encyclopedia/edit-page.html", {
            "form": form,
        })

    return render(request, "encyclopedia/index.html")
