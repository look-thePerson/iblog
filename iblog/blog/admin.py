from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.db.models import Model

from blog.models import Post, Category, Tag
from blog.admin_forms import PostAdminForm
from iblog.site.admin.model_admin import mixin_owner_admin
from iblog.site.custom_admin import Register



class CategoryOwnerFilter(admin.SimpleListFilter):
    """仅展示当前用户分类"""

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(id=self.value())
        return queryset


@Register(Category)
@mixin_owner_admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')
    list_filter = (CategoryOwnerFilter,)

    def save_model(self, request, obj: Category, form, change) -> None:
        obj.owner = request.user
        super(CategoryAdmin, self).save_model(request, obj, form, change)


@Register(Tag)
@mixin_owner_admin
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj: Tag, form, change) -> None:
        obj.owner = request.user
        super(TagAdmin, self).save_model(request, obj, form, change)


@Register(Post)
@mixin_owner_admin
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator'
    ]
    list_display_links = []
    list_filter = ('category__name',)
    search_fields = ['title', 'category__name']
    form = PostAdminForm
    fields = (
        ('category', 'title'),
        'desc', 'status',
        'content', 'tag'
    )

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>',
                           reverse('cus_admin:blog_post_change', args=(obj.id, )))
    operator.short_description = '操作'
