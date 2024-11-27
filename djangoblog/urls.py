# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from blog.views import PostCreateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("", include("accounts.urls")),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path("accounts/", include("django.contrib.auth.urls")),
]


if settings.DEBUG:  # pragma:no cover
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
