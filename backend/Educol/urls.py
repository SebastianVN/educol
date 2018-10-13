from django.conf.urls import url
from Educol import views

urlpatterns = [
    url(r'^usuarios/$', views.UsuarioList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),

    url(r'^evento/$', views.EventoList.as_view()),
    url(r'^evento/(?P<pk>[0-9]+)/$', views.EventoDetail.as_view()),

    url(r'^actividad/$', views.ActividadList.as_view()),
    url(r'^actividad/(?P<pk>[0-9]+)/$', views.ActividadDetail.as_view()),

    url(r'^usuarioevento/$', views.UsuarioEventoList.as_view()),
    url(r'^usuarioevento/(?P<pk>[0-9]+)/$', views.UsuarioEventoDetail.as_view()),
]