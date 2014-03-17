from cms.models import StaticPlaceholder
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin


class StaticPlaceholderAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'code', 'creation_method')
    search_fields = ('name', 'code',)
    exclude = ('creation_method',)
    list_filter = ('creation_method',)

admin.site.register(StaticPlaceholder, StaticPlaceholderAdmin)