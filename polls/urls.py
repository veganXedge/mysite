#file polls/urls
from django.conf.urls import url

from . import views
	
urlpatterns = [
	url(r'^$', views.index, name='index'), #views.py --def index
]										   #point polls.url dir to 
										   #mysite/urls.py
