from django.conf.urls import patterns, include, url
from mysite.views import current_datetime, hours_ahead
from mysite.hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                      ('^$', views.hello),
                      ('^time/?$', current_datetime),
                      (r'^time/plus/(\d{1,2})/?$', hours_ahead),
                      ('^storage/?$', views.save),
                      ('^text/?$', views.text),
                      #remove data
                      #('^remove/?$', views.rem),
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^mysite/', include('mysite.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/',
                       # include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       #url(r'^admin/', include(admin.site.urls)),
                       )
urlpatterns += staticfiles_urlpatterns()
