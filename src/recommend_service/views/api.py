from rest_framework import viewsets

from ..models import Unit, Recommendation
from ..serializers import UnitSerializer, RecommendationSerializer


class BaseViewSet(viewsets.ModelViewSet):
    """ Базовый ViewSet """
    http_method_names = ('get', 'post',)

    def get_authenticators(self):  # создавать могут авторизованные пользователи, просматривать – все
        if self.request.method == 'GET':
            return []
        return super().get_authenticators()

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class UnitViewSet(BaseViewSet):
    """ ViewSet для единицы оценки """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class RecommendationViewSet(BaseViewSet):
    """ ViewSet для рекомендации """
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
