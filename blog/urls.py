from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.poetry_list, name='poetry_list'),
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.post_new, name='post_new'),
]