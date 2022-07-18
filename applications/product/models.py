from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.SlugField(primary_key=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    COUNTRY = (
        ('KG', 'Кыргызстан'),
        ('KZ', 'Казахстан'),
        ('RUS', 'Российская Федерация'),
        ('UKR', 'Украина'),
        ('USA', 'Соединённые Штаты Америки'),
        ('UK', 'Великобритания'),
        ('CN', 'Китай')
    )
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=10)
    author = models.ManyToManyField(User)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='music')
    country = models.CharField(max_length=30, choices=COUNTRY)
    created_at = models.DateField(auto_now_add=True)