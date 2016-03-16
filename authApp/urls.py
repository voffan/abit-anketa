from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.login_web, name = 'login'),
    url(r'^checkuser',views.checkUser, name='checkuser'),
    url(r'^register/$', views.register_index, name="register_index")
]