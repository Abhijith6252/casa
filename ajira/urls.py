# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:47:49 2020

@author: Abhij
"""

from django.conf.urls import url 
from ajira import views 
 
urlpatterns = [ 
    url(r'^api/ajira$', views.cmpginfo_list),
]