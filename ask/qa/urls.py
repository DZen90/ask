from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^login/', views.signin, name='login'),
        url(r'^logout/', logout, {'next_page': '/login'}, name='logout'),
        url(r'^signup/', views.signup, name='signup'),
        url(r'^change_password/', views.change_password, name='change_password'),
        url(r'^question/(?P<question_id>[0-9]+)/', views.question_details, name='question-details'),
        url(r'^ask/', views.ask, name='ask'),
        url(r'^popular/', views.popular, name='popular'),
        url(r'^like/', views.like, name='like'),
        url(r'^search/', views.search, name='search'),
]
