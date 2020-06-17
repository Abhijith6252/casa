from django.db import models

# Create your models here.
class Message(models.Model):
    message_content=models.TextField()
    
    
class CmpgInfo(models.Model):
    tenant_id=models.TextField()
    BU=models.TextField()
    casa_id=models.TextField()
    message=[Message]
    
    
