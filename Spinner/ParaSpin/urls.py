from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'^4/', views.para4, name='para4'),
	url(r'^wikipedia/', views.Wikipedia, name='wikipedia'),
	url(r'^wikichecker/', views.WikiChecker, name='wikichecker')
]
urlpatterns += staticfiles_urlpatterns()