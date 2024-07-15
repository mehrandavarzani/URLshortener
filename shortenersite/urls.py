from django.urls import path,re_path
from . import views
app_name='shortenersite'
urlpatterns=[
    re_path(r'^$',views.index,name='home'),
    re_path(r'^(?P<short_id>\w{6})+?$', views.redirect_original,name='redirectoriginal'),
    re_path(r'^makeshort/$', views.shorten_url,name='shortenurl'),
]