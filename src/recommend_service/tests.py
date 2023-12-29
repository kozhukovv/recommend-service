from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Unit, Recommendation


class UnitViewSetTestCase(APITestCase):
    """ Тестирование UnitViewSet """

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='123')
        self.client.force_authenticate(self.user)

        Unit.objects.create(name='unit-1', description='unit-description-1', author=self.user)
        Unit.objects.create(name='unit-2', description='unit-description-2', author=self.user)

    @classmethod
    def tearDown(cls):
        Unit.objects.all().delete()  # Очистка таблицы Unit после каждого теста

    def test_get_unit_list(self):
        url = reverse('unit-list')  # Получить URL списка рекомендаций
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json['count'], 2)

        for item in response_json['results']:
            self.assertSetEqual(set(item.keys()), {'id', 'name', 'description', 'author'})

    def test_create_unit(self):
        data = {'name': 'Test Unit', 'description': 'Test description'}
        url = reverse('unit-list')  # URL для создания юнита
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка содержимого полей
        unit = Unit.objects.get(name='Test Unit', description='Test description')
        self.assertEqual(unit.name, data['name'])
        self.assertEqual(unit.description, data['description'])


class RecommendationViewSetTestCase(APITestCase):
    """ Тестирование RecommendationViewSet """

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='123')
        self.client.force_authenticate(self.user)

        unit_1 = Unit.objects.create(name='unit-1', description='unit-description-1', author=self.user)
        unit_2 = Unit.objects.create(name='unit-2', description='unit-description-2', author=self.user)

        Recommendation.objects.create(unit=unit_1, stars_count=3, review='some cool review', author=self.user)
        Recommendation.objects.create(unit=unit_2, stars_count=5, review='some cooler review!', author=self.user)

    @classmethod
    def tearDown(cls):
        Unit.objects.all().delete()
        Recommendation.objects.all().delete()  # Очистка таблицы Recommendation после каждого теста

    def test_get_recommendation_list(self):
        url = reverse('recommendation-list')  # Получить URL списка рекомендаций
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json = response.json()
        self.assertEqual(response_json['count'], 2)

        for item in response_json['results']:
            self.assertSetEqual(set(item.keys()), {'id', 'unit', 'stars_count', 'review', 'created_at', 'author'})

    def test_create_recommendation(self):
        unit = Unit.objects.create(name='Test Unit', description='Test description', author=self.user)
        data = {'unit': unit.id, 'stars_count': 5, 'review': 'Great unit!'}
        url = reverse('recommendation-list')  # URL для создания рекомендации
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка содержимого полей
        recommendation = Recommendation.objects.get(unit=unit, stars_count=5, review='Great unit!')
        self.assertEqual(recommendation.unit.id, unit.id)
        self.assertEqual(recommendation.stars_count, data['stars_count'])
        self.assertEqual(recommendation.review, data['review'])
