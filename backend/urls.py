from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogs.views import ListPosts

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ListPosts.as_view(), name='list-blog'),
    url(r'^blogs/', include('blogs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
