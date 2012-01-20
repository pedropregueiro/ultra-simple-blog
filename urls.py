from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
		url(r'^ultra-simple-blog/(\d+)/$', 'ultra-simple-blog.views.show'),
		url(r'^ultra-simple-blog/edit/(\d+)/$', 'ultra-simple-blog.views.edit'),
		url(r'^ultra-simple-blog/delete/(\d+)/$', 'ultra-simple-blog.views.delete'),
		url(r'^ultra-simple-blog/new/$', 'ultra-simple-blog.views.new'),
		url(r'^ultra-simple-blog/$', 'ultra-simple-blog.views.index'),
		url('^$', 'ultra-simple-blog.views.index'),
)