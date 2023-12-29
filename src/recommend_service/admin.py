from django.contrib import admin

from .models import Unit, Recommendation


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    """ Панель администратора для единицы рекомендации """
    search_fields = ('name', 'author__username',)
    list_display = ('name', 'author', 'get_recommendations_count',)


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    """ Панель администратора для рекомендации """
    search_fields = ('author__username', 'unit__name',)
    list_display = ('unit', 'author', 'stars_count',)
    list_filter = ('unit', 'stars_count',)
    autocomplete_fields = ('unit', 'author',)
    readonly_fields = ('created_at',)
