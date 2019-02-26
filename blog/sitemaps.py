from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post

class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Entry.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, item):
        return reverse(item)