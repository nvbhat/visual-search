from django.conf.urls import patterns, include, url
from django.contrib import admin
from drsyasamiksa.views.homepage import HomepageView
from django.conf import settings
#from drsyasamiksa.views.homepage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drsyasamiksa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomepageView.as_view(), name='homepage'),
    #url(r'^homepage/', views.homepage, name='homepage'),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
)
