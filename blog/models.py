import re
from django.db import models
from django.forms import ValidationError
# Create your models here.

def lnglat_validator(value):
    if not re.match('^(\d+\.?\d*),(\d+\.?\d*)?', value):
        raise ValidationError('Invalid LngLat Type')



class Post(models.Model):
    title = models.CharField(max_length=100) # 길이  o
    content = models.TextField() # 길이 x
    tags = models. CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, help_text='위도/경도 포맷으로 입력.',
                             validators=[lnglat_validator], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upgraded_at = models.DateTimeField(auto_now=True)