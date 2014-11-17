from django.conf.urls import patterns, include, url
import os.path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
RESOURCES_PATH =  PROJECT_PATH + '/Resources'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DWT.views.home', name='home'),
    # url(r'^DWT/', include('DWT.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'hello.views.home'),
	( r'^Resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root':RESOURCES_PATH}),

)
