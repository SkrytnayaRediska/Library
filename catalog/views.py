# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Author


def first_view(request):
    authors = Author.objects.all()
    return render(request, "first.html", {"authors": authors})
