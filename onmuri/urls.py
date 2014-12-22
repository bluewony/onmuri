from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from homepage.views import home, photo, media
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='index'),
    url(r'^photo/$', photo, name='photo'),
    url(r'^media/$', media, name='media'),

)


# for development
if settings.DEBUG:
    urlpatterns = urlpatterns + patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )
