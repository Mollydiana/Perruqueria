from django.views.generic import TemplateView
from diana.forms import LoginForm
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from perruqueria import settings



urlpatterns = patterns(
    '',
    # basic urls for templates and registration
    url(r'^$', 'diana.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^servicios/$', 'diana.views.servicios', name='servicios'),
    url(r'^galeria/$', 'diana.views.galeria', name='galeria'),
    url(r'^register/$', 'diana.views.register', name='register'),
    url(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name="fullcalendar"),
    url(r'^schedule/', include('schedule.urls')),



    url(r'^login/$', 'django.contrib.auth.views.login', kwargs={'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': '/'}, name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)