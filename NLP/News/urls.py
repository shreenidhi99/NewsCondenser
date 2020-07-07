from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path,include,re_path
#from . import views
app_name='News'
'''urlpatterns= [ re_path(r'^(?P<genre>Rock|Indie|Metal|Other)/$', views.genre,name="genre"),
               #re_path(r'^(?P<slug>[\w-]+)/$',views.completepost,name="completepost"),
               re_path(r'^(?P<digit>[\d]+)/$',views.completepost,name="completepost"),
               path('createpost',views.post_create,name="create"),]'''


urlpatterns = [
	#path('<int:day><slug:s1><str:month><slug:s2><int:year>/',views.singledate,name="singledate"),
	#path('main/', views.home, name='home'),
	path('<str:date>',views.singledate,name="singledate"),
	path("",views.home,name="home")
	]
	#re_path(r'^(?P<date>[\w-]+)/$',views.singledate,name="singledate")
	
