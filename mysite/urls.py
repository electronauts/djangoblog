# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# админ импортировался django по умолчанию
from django.contrib import admin

# article который есть в urls необходимо также импортировать
import article

admin.autodiscover() 

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
# When we use system stuff (veshi)
# we can write our address to urls.py in quotes
    url(r'^basicview/', include('article.urls')),
## =======Lsen 5. Научим Django понимать к какому view отправлять информацию - urls
    url(r'^', include('article.urls')),
# r'^', - чел просто вбил адрес/ без каких либо параметров
)