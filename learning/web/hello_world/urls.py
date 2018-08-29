# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('html/', views.index, name='html'),
    path('test/', api.test, name='test'),
    path('message/set/', api.set_message, name='set_message'),
    path('message/get/', api.get_message, name='get_message'),
    path('tx/get/', api.tx_look, name='tx_look'),
]
