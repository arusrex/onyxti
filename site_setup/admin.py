from django.contrib import admin
from site_setup.models import SiteSetup

class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Permitir a adição apenas se ainda não existir uma instância
        return not SiteSetup.objects.exists()

    # def has_delete_permission(self, request, obj=None):
    #     # Permitir exclusão (opcional, se você quiser permitir a exclusão)
    #     return super().has_delete_permission(request, obj)

admin.site.register(SiteSetup, SiteSettingsAdmin)
# admin.site.register(SiteSetup)

