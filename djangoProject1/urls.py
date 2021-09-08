from django.contrib import admin
from django.conf.urls import url, include
from djangoProject1 import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url('admin/', admin.site.urls),
    url('FA/', include(('FA.urls', 'FA'))),
    url('about/$', views.about),
    url('home/$', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
