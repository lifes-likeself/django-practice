# Register your models here.

from django.contrib import admin
from .models import Post

# @admin.register(Post)



class PostAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'status', 'content_size', 'created_at', 'upgraded_at']
    actions = ['make_published']

    def content_size(self, Post):
            return '<strong>{}</strong>글자'.format(len(Post.content))

    def make_published(self, request, queryset):
        updated_count = queryset.update(status = 'p')
        self.message_user(request, ' {} sucessfully marked as published'.format(updated_count))
    make_published.short_description = 'Mark selected stories as published'

    content_size.short_description = '글자수'
    #content_size.allow_tags = True


admin.site.register(Post, PostAdmin)




