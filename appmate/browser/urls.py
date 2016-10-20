from django.conf.urls import url

from browser import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blockinfo/$', views.blockinfo, name='blockinfo'),
    url(r'^block/(?P<block_id>\d+)/$', views.getblock, name='detail'),
    url(r'^tx/(?P<tx_id>[\da-f]+)/$', views.gettx, name='tx_detail'),
]
