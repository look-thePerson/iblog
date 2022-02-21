from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from blog.models import Post, Category, Tag
from blog.adminforms import PostAdminForm


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')
    list_filter = (CategoryOwnerFilter,)

    def save_model(self, request, obj: Category, form, change) -> None:
        obj.owner = request.user
        super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj: Tag, form, change) -> None:
        obj.owner = request.user
        super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
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
                           reverse('admin:blog_post_change', args=(obj.id, )))
    operator.short_description = '操作'

    def save_model(self, request, obj: Category, form, change) -> None:
        obj.owner = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        return super(PostAdmin, self).get_queryset(request).filter(owner=request.user)
