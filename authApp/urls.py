from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$',views.login_web, name = 'login'),
	url(r'^checkUserValid',views.checkUserValid, name='checkUserValid'),
	url(r'^checkEmailValid',views.checkEmailValid, name='checkEmailValid'),
	url(r'^register/$', views.register_index, name="register_index")
]