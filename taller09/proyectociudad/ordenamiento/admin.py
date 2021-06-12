from django.contrib import admin

from ordenamiento.models import Parroquia, Barrio
from import_export.admin import ImportExportModelAdmin

class ParroquiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'num_viviendas', 'num_parques', 'num_edificios')
    search_fields = ('nombre', 'num_parques')

admin.site.register(Barrio, BarrioAdmin)
