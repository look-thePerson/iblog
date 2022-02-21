from django.contrib import admin

from config.models import Link, SideBar
from utils.custom_site import Register


@Register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)


@Register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)
