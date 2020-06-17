# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:41:34 2020

@author: Abhij
"""

from rest_framework import serializers 
from ajira.models import CmpgInfo
from ajira.models import Message
 
 
class CmpgInfoSerializer(serializers.ModelSerializer):
 
    class Meta:
        
        model=CmpgInfo
        fields = ('id','tenant_id','BU','casa_id','message')
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=('id','message_content')