# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')
