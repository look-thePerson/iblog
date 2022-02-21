from django.contrib.admin import AdminSite
from django.db.models import Model
from django.contrib import admin


class CustomAdminSite(AdminSite):
    site_header = 'IBlog'
    site_title = 'IBlog 管理后台'
    index_title = '首页'


class Register:

    site = CustomAdminSite("cus_admin")

    def __init__(self, model :Model) -> None:
        self.registe_hanlder = admin.register(model, site=Register.site)

    def __call__(self, model_admin: admin.ModelAdmin):
        return self.registe_hanlder(model_admin)


custom_site = Register.site
