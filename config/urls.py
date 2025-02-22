from django.conf import settings
from django.urls import include, path, re_path, register_converter
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from etna.records import converters
from etna.records import views as records_views

register_converter(converters.ReferenceNumberConverter, "reference_number")
register_converter(converters.IAIDConverter, "iaid")

# fmt: off
urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),

    path("documents/", include(wagtaildocs_urls)),

    path(
        r"catalogue/<iaid:iaid>/",
        login_required(records_views.record_page_view),
        name="details-page-machine-readable",
    ),
    path(
        r"catalogue/<reference_number:reference_number>/",
        login_required(records_views.record_page_disambiguation_view),
        name="details-page-human-readable",
    ),

    path(
        "records/image/<path:location>",
        records_views.image_serve,
        name="image-serve",
    ),

    path(
        r"records/images/<iaid:iaid>/<str:sort>/",
        login_required(records_views.image_viewer),
        name="image-viewer",
    ),

    path(
        r"records/images/<iaid:iaid>/",
        login_required(records_views.image_browse),
        name="image-browse",
    ),
]
# fmt: on


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    path('accounts/', include('allauth.urls')),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
