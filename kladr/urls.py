from django.conf.urls import patterns, include, url

from kladr import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'narcology.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #===============================================ajax==========================================================
    url(r'^get_region$',views.get_region, name='get_region'),
    url(r'^get_district$',views.get_district, name='get_district'),
    url(r'^get_city$',views.get_city, name='get_city'),
    url(r'^get_street$',views.get_street, name='get_street'),
    url(r'^get_village$',views.get_village, name='get_village'),
    url(r'^get_homes$',views.get_homes, name='get_homes'),
    url(r'^get_objects_by_id$',views.get_objects_by_id, name='get_objects_by_id'),
)
