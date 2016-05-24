from django.conf.urls import url

from . import views

urlpatterns = [
 # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^gnuplot$', views.gnuplot, name='gnuplot'),
    url(r'^gnuplot/windows$', views.gnuplotw, name='gnuplotw'),
    url(r'^gnuplot/linux$', views.gnuplotl, name='gnuplotl'),
    url(r'^gnuplot/osx$', views.gnuploto, name='gnuploto'),
]

