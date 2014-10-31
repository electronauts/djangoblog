from django.conf.urls import patterns, include, url
#
from django.contrib import admin

# we should import our app article
# it is unnececesarly to import app
import article

admin.autodiscover() 

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
# When we use system stuff (veshi)
# we can write our address to urls.py in quotes
    url(r'^basicview/', include('article.urls')),
)

