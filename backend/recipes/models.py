from django.db import models


class Entity(models.Model):
    """Abstract business logic entity class."""
    name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Measure(models.Model):
    """Ingredients measurement unit."""
    name = models.CharField(
        max_length=10, unique=True, verbose_name='Название'
    )
    description = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Описание'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Мера'
        verbose_name_plural = 'Меры'

    def __str__(self):
        return self.name


class Ingredient(Entity):
    """Recipe ingredient model."""
    measurement_unit = models.ForeignKey(
        Measure, on_delete=models.PROTECT, verbose_name='Мера'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
