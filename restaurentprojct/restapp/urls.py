from django.urls import path

import restapp
from . import views
from django.conf.urls import url

app_name = 'restapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('rest/<int:rest_id>/',views.detail,name='detail'),
    path('add/',views.addfood,name='addfood'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]