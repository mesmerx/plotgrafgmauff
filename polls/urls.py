from django.conf.urls import url

from . import views

urlpatterns = [
 # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^sagemath$', views.sagemath, name='sagemath'),

    url(r'^gnuplot$', views.gnuplot, name='gnuplot'),
    url(r'^gnuplot/windows$', views.gnuplotw, name='gnuplotw'),
    url(r'^gnuplot/linux$', views.gnuplotl, name='gnuplotl'),
    url(r'^gnuplot/osx$', views.gnuploto, name='gnuploto'),
    url(r'^gnuplot/limites$', views.gnuplotlimit, name='gnuplotlimit'),
    url(r'^gnuplot/doiseixos$', views.gnuplotdoiseixos, name='gnuplotdoiseixos'),
    url(r'^gnuplot/treseixos$', views.gnuplottreseixos, name='gnuplottreseixos'),
    url(r'^gnuplot/multiplot$', views.gnuplotmulti, name='gnuplotmulti'),
    url(r'^gnuplot/parametrica$', views.gnuplotparametrica, name='gnuplotparametrica'),
    url(r'^gnuplot/gnuplotcondicionais$', views.gnuplotcondicionais, name='gnuplotcondicionais'),
    url(r'^gnuplot/repeticoes$', views.gnuplotrepeticoes, name='gnuplotrepeticoes'),
    url(r'^gnuplot/macros$', views.gnuplotmacros, name='gnuplotmacros'),
    url(r'^gnuplot/arquivos$', views.gnuplotarquivos, name='gnuplotarquivos'),
    url(r'^sagemath/windows$', views.sagewindows, name='sagewindows'),
    url(r'^sagemath/linux$', views.sagelinux, name='sagelinux'),
    url(r'^sagemath/mac$', views.sagemac, name='sagemac'),
]

