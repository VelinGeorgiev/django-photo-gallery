from django.contrib import sitemaps
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from app.models import Album, AlbumImage

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['gallery']

    def location(self, item):
        return reverse(item)

class AlbumViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Album.objects.filter(is_visible=True)

    def lastmod(self, obj):
        return obj.modified

    def location(self, item):
        return reverse("album", kwargs={"album_slug": item.slug})

class ImagesViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        albums = Album.objects.filter(is_visible=True)
        list = []
        for album in albums:
            images = AlbumImage.objects.filter(album__id=album.id)
            list.append({
                'title': album.title,
                 #'caption': album.description,
                 #'geo_location': '{0}, {1}'.format(album.area, album.get_album_category_display()),
                 'images': images,
                 'slug': album.slug ,
                 'created': album.modified
                 })
        return list

    def lastmod(self, obj):
        return obj['created']

    def location(self, item):
        return reverse("album", kwargs={"album_slug": item['slug']})