from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loading', views.loading, name='loading'),
    path('result/<source>/<int:isfake>', views.result, name='result'),
    path('runMain/<source>/<text>', views.runMain, name='runMain'),
    # path('modelCaller', views.modelCaller, name='modelCaller'),
]

 