from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dados.views import contato


urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html")),
    path("admin/", admin.site.urls),
    path("", include("dados.urls"), name="dados"),
    path('contato/', contato, name='contato'),
    # terceiros
    path("ckeditor/", include("ckeditor_uploader.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
