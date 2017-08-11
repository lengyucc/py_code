from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),	# http://localhost:8000/polls/123123/
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),	# http://localhost:8000/polls/123123/results/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),	# http://localhost:8000/polls/123123/vote/
]
