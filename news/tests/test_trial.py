# news/tests/test_trial.py
from unittest import skip
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from news.models import News

User = get_user_model()

@skip
# Создаём тестовый класс с произвольным названием, наследуем его от TestCase.
class TestNews(TestCase):
    # Все нужные переменные сохраняем в атрибуты класса.
    TITLE = 'Заголовок новости'
    TEXT = 'Тестовый текст'

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testUser')
        cls.user_client = Client()
        cls.user_client.force_login(cls.user)

    @classmethod
    def setUpTestData(cls):
        # Стандартным методом Django ORM create() создаём объект класса.
        # Присваиваем объект атрибуту класса: назовём его news.
        cls.news = News.objects.create(
            title=cls.TITLE,
            text=cls.TEXT,
        )

    # Проверим, что объект действительно было создан.
    # def test_successful_creation(self):
    #     # При помощи обычного ORM-метода посчитаем количество записей в базе.
    #     news_count = News.objects.count()
    #     # Сравним полученное число с единицей.
    #     self.assertEqual(news_count, 1)
    #
    # def test_title(self):
    #     self.assertEqual(self.news.title, self.TITLE, 'Неправильный заголовок!')
