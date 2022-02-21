from django.contrib import admin

from comment.models import Comment
from iblog.site.admin.model_admin import mixin_owner_admin
from iblog.site.custom_admin import Register

@Register(Comment)
@mixin_owner_admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
