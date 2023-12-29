from rest_framework import serializers

from .models import Unit, Recommendation


class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = ('id', 'unit', 'stars_count', 'review', 'created_at', 'author',)
        read_only_fields = ('created_at', 'author',)


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ('id', 'name', 'description', 'author',)
        read_only_fields = ('author',)
