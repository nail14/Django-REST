from django.test import TestCase

# Create your tests here.
import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import CustomUserModelViewSet
from .models import User, Biography


class TestUserViewSet(TestCase):
    # url = '/api/users/'

    def setUP(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.data = {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 1799}
        self.data_put = {'first_name': 'Андрей', 'last_name': 'Ананич', 'birthday_year': 1985}
        self.url = '/api/users/'
        self.admin = User.objects.create_superuser(self.name, 'admin@mail.ru', self.password)

    def test_get_list(self):
        # создаем объект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса
        request = factory.get(self.url)
        # указываем как тип запроса будет передано в AuthorModelViewSet
        view = CustomUserModelViewSet.as_view({'get': 'list'})
        # передаем во вью и получаем ответ
        response = view(request)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        # создаем объект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса
        # data = {'first_name': 'Александр','last_name': 'Пушкин', 'birthday_year': 1799}
        request = factory.post(self.url, self.data, format='json')
        # указываем как тип запроса будет передано в AuthorModelViewSet
        view = CustomUserModelViewSet.as_view({'post': 'create'})
        # передаем во вью и получаем ответ
        response = view(request)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        # создаем объект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса

        request = factory.post(self.url, self.data, format='json')
        # авторизоваться
        force_authenticate(request, self.admin)
        # указываем как тип запроса будет передано в AuthorModelViewSet
        view = CustomUserModelViewSet.as_view({'post': 'create'})
        # передаем во вью и получаем ответ
        response = view(request)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        # создаем объект класса APIClient
        client = APIClient()
        #создаем юсера через DRM для проверки детализации
        user = User.objects.create(**self.data)
        # сделать запрос
        response = client.get(f'{self.url}{user.id}/')
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_guest(self):
        # создаем объект класса APIClient
        client = APIClient()
        #создаем юсера через DRM для проверки обновления
        user = User.objects.create(**self.data)
        # сделать запрос
        response = client.put(f'{self.url}{user.id}/',self.data_put)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_admin(self):
        # создаем объект класса APIClient
        client = APIClient()
        #создаем юсера через DRM для проверки обновления
        user = User.objects.create(**self.data)
        #авторизация
        client.login(username=self.name, password=self.password)
        # сделать запрос
        response = client.put(f'{self.url}{user.id}/',self.data_put)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем юсера
        user_update = User.objects.get(id=user.id)
        # сделать проверку
        self.assertEqual(user_update.first_name, 'Андрей')
        self.assertEqual(user_update.last_name, 'Ананич')
        self.assertEqual(user_update.birthday_year, 1985)
        client.logout()





    def tearDown(self) -> None:
        pass


class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        response = math.sqrt(4)
        self.assertEqual(response,2)

class TestBiographyViewSet(APITestCase):

    def setUP(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.data = {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 1799}
        self.data_put = {'first_name': 'Андрей', 'last_name': 'Ананич', 'birthday_year': 1985}
        self.url = '/api/biography/'
        self.admin = User.objects.create_superuser(self.name, 'admin@mail.ru', self.password)

    def test_get_list(self):
        # создаем запрос
        response = self.client.get(self.url)
        # проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        # создаем автора через ORM для связи с биографией
        user = User.objects.create(**self.data)
        # создание биографии
        bio = Biography.objects.create(text='test', user=user)
        # авторизоваться
        self.client.login(username=self.name, password=self.password)
        # запрос
        response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'user': bio.user.id})
        # проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем биографию
        biog = Biography.objects.get(id=bio.id)
        # сделать проверку
        self.assertEqual(biog.text, 'Biography')
        # разлогинимся
        self.client.logout()

    def test_edit_mixer(self):
        # создание биографии
        bio = mixer.blend(Biography)
        # авторизоваться
        self.client.login(username=self.name, password=self.password)
        # запрос
        response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'user': bio.user.id})
        # проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем биографию
        biog = Biography.objects.get(id=bio.id)
        # сделать проверку
        self.assertEqual(biog.text, 'Biography')
        # разлогинимся
        self.client.logout()

    def test_edit_mixer(self):
        # создание биографии
        bio = mixer.blend(Biography, text='Вася')
        # авторизоваться
        self.client.login(username=self.name, password=self.password)
        # запрос
        response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'user': bio.user.id})
        # проверяем ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем биографию
        biog = Biography.objects.get(id=bio.id)
        # сделать проверку
        self.assertEqual(biog.text, 'Biography')
        # разлогинимся
        self.client.logout()


