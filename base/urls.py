from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    # url(r'^login/$', include('django.contrib.auth.views.login')),
    # url(r'^logout/$', include('django.contrib.auth.views.logout')),
]
