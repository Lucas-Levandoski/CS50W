from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def viewPage(request, title):
    entry = util.get_entry(title)

    if entry == None:
        return render(request, "encyclopedia/not-found.html", {
            "title": "Not Found"
        })

    return render(request, "encyclopedia/wiki-page.html", {
        "title": title,
        "entry": entry,
    })
