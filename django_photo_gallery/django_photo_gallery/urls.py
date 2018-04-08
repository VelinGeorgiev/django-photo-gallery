from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from app.sitemaps import StaticViewSitemap, AlbumViewSitemap, ImagesViewSitemap
sitemaps = {
    'static': StaticViewSitemap,
    'albums': AlbumViewSitemap
}

import app.forms
import app.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.gallery, name='gallery'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    url(r'^(?P<slug>[-\w]+)$', app.views.AlbumDetail.as_view(), name='album'),

    # seo
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    url(r'^sitemap\.xml$', never_cache(sitemap), {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^images-sitemap\.xml$', never_cache(sitemap), { 'sitemaps': {'images': ImagesViewSitemap }, 'template_name': 'images_sitemap.html' }, name='images_sitemap'),

    # admin
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, { 'next_page': '/', }, name='logout'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



