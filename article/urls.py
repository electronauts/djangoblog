from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.template_two'),
    url(r'^3/', 'article.views.template_three_simple'),
)

# Na nashu functiu basic_one ssilayetsya basicview/1/
# Django znayet shto 1 eto article.vies.basic_one