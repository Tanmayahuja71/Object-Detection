from django.db import models
import datetime
# A UUID (Universal Unique Identifier) is a 128-bit value used to uniquely identify an object or entity on the internet.
import uuid
# Create your models here.
class Account(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    username = models.CharField(max_length=100,null=False,blank=False)
    first_name = models.CharField(max_length=100,null=False,blank=False)
    last_name = models.CharField(max_length=100,null=False,blank=False)
    phone_number=models.IntegerField(null=True)
    is_email_verified = models.BooleanField(default=False)
    email_id = models.EmailField(null=True,blank=True)
    user_password=models.CharField(max_length=100,null=True,blank=False)