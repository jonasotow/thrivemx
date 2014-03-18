from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('thrive.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^nosotros/$','nosotros_view',name='vista_nosotros'),

)