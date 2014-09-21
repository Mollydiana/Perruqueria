from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from perruqueria import settings



urlpatterns = patterns('',

    url(r'^$', 'diana.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cita/$', 'diana.views.cita', name='cita'),
    url(r'^contacto/$', 'diana.views.contacto', name='contacto'),
    url(r'^test/$', 'diana.views.test', name='test'),



    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),

    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)