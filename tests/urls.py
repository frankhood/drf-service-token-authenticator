# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    path("api/v1/", include("tests.example.api.urls")),
]
