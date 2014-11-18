# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.template_two'),
    url(r'^3/', 'article.views.template_three_simple'),
#==== l5 Научим Django понимать, что делать когда в адресной строке будет:
    url(r'^articles/all/$', 'article.views.articles'),
# r - означает, что дальше идет регулярное выражение
# ^ - знак начала строки, т.е. все что идет после домена.
# $ - означает конец строки
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
# Хитрое выражение. Запомните его. Оно означает, что то что идет после / будет являться переменной, которую мы передадим в качестве параметра функции - article_id во views Для этого используется знак вопроса и потом имя переменной. Кроме того нам необходимо указать, что данная переменная должна являться цифрой \d+/ конец строки.
)

# Na nashu functiu basic_one ssilayetsya basicview/1/
# Django znayet shto 1 eto article.vies.basic_one