from django.contrib import admin

from comment.models import Comment
from utils.custom_site import Register

@Register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
