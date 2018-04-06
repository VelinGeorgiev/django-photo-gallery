from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.gallery, name='gallery'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    url(r'^(?P<slug>[-\w]+)$', app.views.AlbumDetail.as_view(), name='album'),
     
    # admin
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, { 'next_page': '/', }, name='logout'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



