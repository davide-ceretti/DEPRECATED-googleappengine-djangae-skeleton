from django.conf.urls import patterns, include, url
from django.contrib import admin

from application.crud import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^_ah/', include('djangae.urls')),
    url(r'^$', views.ItemCreateView.as_view(), name='index'),
)
