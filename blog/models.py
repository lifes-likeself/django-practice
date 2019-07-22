import re
from django.db import models
from django.forms import ValidationError
# Create your models here.

def lnglat_validator(value):
    if not re.match('^(\d+\.?\d*),(\d+\.?\d*)?', value):
        raise ValidationError('Invalid LngLat Type')

#

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100) # 길이  o
    content = models.TextField() # 길이 x
    tags = models. CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, help_text='위도/경도 포맷으로 입력.',
                             validators=[lnglat_validator], blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    upgraded_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE,)
        author = models.CharField(max_length=20)
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        upgraded_at = models.DateTimeField(auto_now=True)

class Meta:
            ordering = ['id']


