import re
from django.db import models
from django.forms import ValidationError
from django.conf import settings

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

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_post_set')
    #author = models.CharField(max_length=30)
    title = models.CharField(max_length=100) # 길이  o
    content = models.TextField() # 길이 x
    tags = models. CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, help_text='위도/경도 포맷으로 입력.',
                             validators=[lnglat_validator], blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    Tag_set = models.ManyToManyField('Tag')
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

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Meta:
            ordering = ['id']


