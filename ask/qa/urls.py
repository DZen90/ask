from django.conf.urls import url

from . import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^login/', views.test, name='test'),
        url(r'^signup/', views.test, name='test'),
        url(r'^question/(?P<question_id>[0-9]+)/', views.question_details, name='question-details'),
        url(r'^ask/', views.ask, name='ask'),
        url(r'^popular/', views.popular, name='popular'),
        #url(r'^new/', views.test, name='test'),
]
