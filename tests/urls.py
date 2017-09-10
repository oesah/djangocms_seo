# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from djangocms_seo.urls import urlpatterns as djangocms_seo_urls

urlpatterns = [
    url(r'^', include(djangocms_seo_urls, namespace='djangocms_seo')),
]
