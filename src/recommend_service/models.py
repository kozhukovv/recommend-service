from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Unit(models.Model):
    """ Единица рекомендации """
    name = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        verbose_name='Наименование',
    )

    description = models.TextField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name='Описание',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
        related_name='units',
        verbose_name='Автор',
    )

    def get_recommendations_count(self):
        """ Получение счетчика рекомендаций товара """
        return self.recommendations.count()

    class Meta:
        verbose_name = 'Единица оценки'
        verbose_name_plural = 'единицы оценки'

    def __str__(self):
        return self.name


class Recommendation(models.Model):
    """ Рекомендация """
    unit = models.ForeignKey(
        Unit,
        null=False,
        on_delete=models.CASCADE,
        related_name='recommendations',
        verbose_name='Единица рекомендации',
    )

    stars_count = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1), MaxValueValidator(5)
        ],
        verbose_name='Количество звезд',
    )

    review = models.TextField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name='Отзыв',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
        related_name='recommendations',
        verbose_name='Автор',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано',
    )

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'рекомендации'

    def __str__(self):
        return f'{self.author.username}: {self.unit.name}'
