from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from admin_auto_filters.filters import AutocompleteFilter

from festival.models import Festival, Encontro, Categoria, Atividade, Tag
from festival.forms import AtividadeAdminForm

class EncontroFilter(AutocompleteFilter):
    title = 'Encontro'
    field_name = 'encontro'

class CategoriasFilter(AutocompleteFilter):
    title = 'Categoria'
    field_name = 'categorias'

class TagsFilter(AutocompleteFilter):
    title = 'Tags'
    field_name = 'tags'

class RedeFilter(AutocompleteFilter):
    title = 'Rede'
    field_name = 'rede'

class ResponsavelFilter(AutocompleteFilter):
    title = 'Responsável'
    field_name = 'responsavel'

class ConvidadeFilter(AutocompleteFilter):
    title = 'Convidade'
    field_name = 'convidades'

class EspacoFilter(AutocompleteFilter):
    title = 'Espaço'
    field_name = 'espaco'

class AtividadeAdmin(admin.ModelAdmin):
    form = AtividadeAdminForm
    list_filter = ['pendente', EspacoFilter, EncontroFilter, CategoriasFilter, TagsFilter, RedeFilter, ResponsavelFilter, ConvidadeFilter]
    list_display = ['titulo', 'espaco', 'inicio_fmt', 'fim_fmt', 'coluna', 'convidades_list']
    search_fields = ['titulo', 'descricao']
    autocomplete_fields = ['categorias', 'tags', 'responsavel', 'convidades']
    save_on_top = True

    def convidades_list(self, obj):
        return obj.convidades.count()
    convidades_list.short_description = '# convidades'

    def inicio_fmt(self, obj):
        try:
            return obj.inicio.strftime("%d/%m %H:%M")
        except AttributeError:
            return '-'
    def fim_fmt(self, obj):
        try:
            return obj.fim.strftime("%d/%m %H:%M")
        except AttributeError:
            return '-'
    inicio_fmt.short_description = 'início'
    fim_fmt.short_description = 'fim'
    inicio_fmt.admin_order_field = 'inicio'
    fim_fmt.admin_order_field = 'fim'

    class Media:
        pass

class TagAdmin(admin.ModelAdmin):
    search_fields = ['nome']

class CategoriaAdmin(DraggableMPTTAdmin):
    search_fields = ['nome', 'parent__nome']
    mptt_indent_field = "some_node_field"


admin.site.register(Festival)
admin.site.register(Encontro)
admin.site.register(Tag, TagAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Atividade, AtividadeAdmin)
