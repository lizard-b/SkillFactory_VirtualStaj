import random
from unittest import TestCase

from django.urls import reverse

import factory
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import *


class TouristApiTestCase(APITestCase):
    def setUp(self):
        self.user_1 = Tourist.objects.create(email='email1@mail.ru',
                                             last_name='Lastname1',
                                             first_name='Name1',
                                             patronymic='Patronymic1',
                                             phone='89210000001')
        self.user_2 = Tourist.objects.create(email='email2@mail.ru',
                                             last_name='Lastname2',
                                             first_name='Name2',
                                             patronymic='Patronymic2',
                                             phone='89210000002')

    def test_get_list(self):
        url = reverse('tourist-list')
        response = self.client.get(url)
        serializer_data = TouristSerializer([self.user_1, self.user_2], many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(len(serializer_data), 2)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('tourist-detail', args=(self.user_1.id,))
        response = self.client.get(url)
        serializer_data = TouristSerializer(self.user_1).data
        print(serializer_data)
        print(response.data)
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)


class CoordinatesApiTestCase(APITestCase):
    def setUp(self):
        self.coords_1 = Coordinates.objects.create(latitude='11.11', longitude='11.11', elevation=111)
        self.coords_2 = Coordinates.objects.create(latitude='22.22', longitude='22.22', elevation=222)

    def test_get_list(self):
        url = reverse('coordinates-list')
        response = self.client.get(url)
        serializer_data = CoordinatesSerializer([self.coords_1, self.coords_2], many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(len(serializer_data), 2)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('coordinates-detail', args=(self.coords_1.id,))
        response = self.client.get(url)
        serializer_data = CoordinatesSerializer(self.coords_1).data
        print(serializer_data)
        print(response.data)
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)


class LevelApiTestCase(APITestCase):
    def setUp(self):
        self.lvl_1 = Level.objects.create(winter='1A', spring='1A', summer='1A', autumn='1A')
        self.lvl_2 = Level.objects.create(winter='2A', spring='2A', summer='2A', autumn='2A')

    def test_get_list(self):
        url = reverse('level-list')
        response = self.client.get(url)
        serializer_data = LevelSerializer([self.lvl_1, self.lvl_2], many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(len(serializer_data), 2)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('level-detail', args=(self.lvl_1.id,))
        response = self.client.get(url)
        serializer_data = LevelSerializer(self.lvl_1).data
        print(serializer_data)
        print(response.data)
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(id=1, beauty_title='BTitle_1', title='BT_1', other_titles='BT_11',
                                                connect='Connects', add_time='2024-05-28T11:11:11.853Z', status='NW',
                                                user=Tourist.objects.create(email='email1@mail.ru',
                                                                            last_name='Lastname1',
                                                                            first_name='Name1',
                                                                            patronymic='Patronymic1',
                                                                            phone='89210000001'),
                                                coords=Coordinates.objects.create(latitude='11.11', longitude='11.11',
                                                                                  elevation=111),
                                                level=Level.objects.create(winter='1A', spring='1A', summer='1A',
                                                                           autumn='1A'))
        self.pereval_2 = Pereval.objects.create(id=2, beauty_title='BTitle_2', title='BT_2', other_titles='BT_22',
                                                connect='Connects', add_time='2024-05-28T22:22:22.853Z', status='NW',
                                                user=Tourist.objects.create(email='email2@mail.ru',
                                                                            last_name='Lastname2',
                                                                            first_name='Name2',
                                                                            patronymic='Patronymic2',
                                                                            phone='89210000002'),
                                                coords=Coordinates.objects.create(latitude='22.22', longitude='22.22',
                                                                                  elevation=222),
                                                level=Level.objects.create(winter='2A', spring='2A', summer='2A',
                                                                           autumn='2A'))

    def test_get_list(self):
        url = reverse('pereval-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(len(serializer_data), 2)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('pereval-detail', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        print(serializer_data)
        print(response.data)
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)


class TouristSerializerTestCase(TestCase):
    def setUp(self):
        self.user_1 = Tourist.objects.create(email='email1@mail.ru',
                                             last_name='Lastname1',
                                             first_name='Name1',
                                             patronymic='Patronymic1',
                                             phone='89210000001')
        self.user_2 = Tourist.objects.create(email='email2@mail.ru',
                                             last_name='Lastname2',
                                             first_name='Name2',
                                             patronymic='Patronymic2',
                                             phone='89210000002')

    def test_check(self):
        serializer_data = TouristSerializer([self.user_1, self.user_2], many=True).data
        expected_data = [

            {
                'email': 'email1@mail.ru',
                'last_name': 'Lastname1',
                'first_name': 'Name1',
                'patronymic': 'Patronymic1',
                'phone': '89210000001'
            },
            {
                'email': 'email2@mail.ru',
                'last_name': 'Lastname2',
                'first_name': 'Name2',
                'patronymic': 'Patronymic2',
                'phone': '89210000002'
            }
        ]
        self.assertEquals(serializer_data, expected_data)


class CoordinatesSerializerTestCase(TestCase):
    def setUp(self):
        self.coords_1 = Coordinates.objects.create(latitude='11.11111111', longitude='11.11111111', elevation=111)
        self.coords_2 = Coordinates.objects.create(latitude='22.22222222', longitude='22.22222222', elevation=222)

    def test_check(self):
        serializer_data = CoordinatesSerializer([self.coords_1, self.coords_2], many=True).data
        expected_data = [

            {
                'latitude': '11.11111111',
                'longitude': '11.11111111',
                'elevation': 111
            },
            {
                'latitude': '22.22222222',
                'longitude': '22.22222222',
                'elevation': 222
            }
        ]
        self.assertEquals(serializer_data, expected_data)


class LevelSerializerTestCase(TestCase):
    def setUp(self):
        self.lvl_1 = Level.objects.create(winter='1A', spring='1A', summer='1A', autumn='1A')
        self.lvl_2 = Level.objects.create(winter='2A', spring='2A', summer='2A', autumn='2A')

    def test_check(self):
        serializer_data = LevelSerializer([self.lvl_1, self.lvl_2], many=True).data
        expected_data = [

            {
                'winter': '1A',
                'spring': '1A',
                'summer': '1A',
                'autumn': '1A'
            },
            {
                'winter': '2A',
                'spring': '2A',
                'summer': '2A',
                'autumn': '2A'
            }
        ]
        self.assertEquals(serializer_data, expected_data)


class PerevalSerializerTestCase(TestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(beauty_title='BTitle_1', title='BT_1', other_titles='BT_11',
                                                connect='Connects1',
                                                add_time='%d-%m-%Y %H:%M:%S',
                                                status='NW',
                                                user=Tourist.objects.create(email='email1@mail.ru',
                                                                            last_name='Lastname1',
                                                                            first_name='Name1',
                                                                            patronymic='Patronymic1',
                                                                            phone='89210000001'),
                                                coords=Coordinates.objects.create(latitude='11.11111111',
                                                                                  longitude='11.11111111',
                                                                                  elevation=111),
                                                level=Level.objects.create(winter='1A', spring='1A', summer='1A',
                                                                           autumn='1A'),
                                                )
        self.images_1 = PerevalImage.objects.create(images='image1.jpg', pereval=self.pereval_1, title='imagetitle1')

        self.pereval_2 = Pereval.objects.create(beauty_title='BTitle_2', title='BT_2', other_titles='BT_22',
                                                connect='Connects2',
                                                add_time='%d-%m-%Y %H:%M:%S',
                                                status='NW',
                                                user=Tourist.objects.create(email='email2@mail.ru',
                                                                            last_name='Lastname2',
                                                                            first_name='Name2',
                                                                            patronymic='Patronymic2',
                                                                            phone='89210000002'),
                                                coords=Coordinates.objects.create(latitude='22.22222222',
                                                                                  longitude='22.22222222',
                                                                                  elevation=222),
                                                level=Level.objects.create(winter='2A', spring='2A', summer='2A',
                                                                           autumn='2A'))
        self.images_2 = PerevalImage.objects.create(images='image2.jpg', pereval=self.pereval_2, title='imagetitle2')

    def test_check(self):
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        expected_data = [

            {
                'id': self.pereval_1.id,
                'beauty_title': 'BTitle_1',
                'title': 'BT_1',
                'other_titles': 'BT_11',
                'connect': 'Connects1',
                'add_time': self.pereval_1.add_time.strftime('%d-%m-%Y %H:%M:%S'),
                'status': 'NW',
                'user': {'email': 'email1@mail.ru', 'last_name': 'Lastname1', 'first_name': 'Name1',
                         'patronymic': 'Patronymic1', 'phone': '89210000001'},
                'coords': {'latitude': '11.11111111', 'longitude': '11.11111111', 'elevation': 111},
                'level': {'winter': '1A', 'spring': '1A', 'summer': '1A', 'autumn': '1A'},
                'images': [
                    {'images': 'image1.jpg', 'title': 'imagetitle1'},
                ]
            },
            {
                'id': self.pereval_2.id,
                'beauty_title': 'BTitle_2',
                'title': 'BT_2',
                'other_titles': 'BT_22',
                'connect': 'Connects2',
                'add_time': self.pereval_2.add_time.strftime('%d-%m-%Y %H:%M:%S'),
                'status': 'NW',
                'user': {'email': 'email2@mail.ru', 'last_name': 'Lastname2', 'first_name': 'Name2',
                         'patronymic': 'Patronymic2', 'phone': '89210000002'},
                'coords': {'latitude': '22.22222222', 'longitude': '22.22222222', 'elevation': 222},
                'level': {'winter': '2A', 'spring': '2A', 'summer': '2A', 'autumn': '2A'},
                'images': [
                    {'images': 'image2.jpg', 'title': 'imagetitle2'},
                ]
            }
        ]

        self.assertEquals(serializer_data, expected_data)


# Create your tests here.
