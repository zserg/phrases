from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from ruseng import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('^about/$', views.about, name='about'),
    url('^profile/$', views.profile, name='ruseng.views.profile'),
    url('^get_data/$', views.get_data, name='get-data'),
    url('^settings/$', views.settings, name='settings'),

]


