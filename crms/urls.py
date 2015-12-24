from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from cr.views import login, register, result, aboutus, tomap, detail, \
personal, logout, submit, select, add, finishAdd,delete,showall
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login),
    url(r'^register/$', register),
    url(r'^select/$', select),
    url(r'^result(\d+)/$', result, name="result"),
    url(r'^aboutus/$', aboutus),
    url(r'^map/$', tomap),
    url(r'^detail(\d+)/$',detail, name="detail"),
    url(r'^personal/$',personal),
    url(r'^logout/$',logout),
    url(r'^submit(\d+)/$',submit, name="submit"),
    url(r'^add(\d+)/$', add ,name = "add"),
    url(r'^finishAdd(\d+)/$', finishAdd ,name = "finishAdd"),
    url(r'^delete(\d+)/$',delete, name = "delete"),
    url(r'^showall(\d+)/$',showall, name = "showall"),
#url(r'^$', views.register, name='register'),
    )
