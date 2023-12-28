# pylint: disable=all
from django.apps import AppConfig


class RecommendServiceConfig(AppConfig):
    """ Управление тегами """
    name = 'recommend_service'
    verbose_name = 'Сервис рекомендаций'
