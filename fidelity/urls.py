# fidelity/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("base.urls", "base"), "base")),
]

# ESTA PARTE É ESSENCIAL PARA O CSS FUNCIONAR COM DEBUG=FALSE
if settings.DEBUG is False:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
    ]