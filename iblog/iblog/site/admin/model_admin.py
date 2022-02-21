from django.contrib.admin import ModelAdmin
from django.db.models import Model

from utils.mixin import mixin


def mixin_owner_admin(model_admin_cls) -> ModelAdmin:
    """
        需要在注册ModelAdmin以前使用
        混入过滤非自己资源的能力
        要求对应的Model定义了owner字段
    """

    cls = model_admin_cls

    def save_model(self: ModelAdmin, request, obj: Model, form, change) -> None:
        obj.owner = request.user
        super(cls, self).save_model(request, obj, form, change)

    def get_queryset(self: ModelAdmin, request):
        return super(cls, self).get_queryset(request).filter(owner=request.user)

    return mixin(save_model, get_queryset)(cls)
