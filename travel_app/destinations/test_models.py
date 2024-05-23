from django.test import TestCase
from .models import Destination
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


#unit testing

class DestinationModelTest(TestCase):
    def test_destination_creation(self):
        destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Beach',
            image_url='https://example.com/image.jpg'
        )
        self.assertEqual(destination.name, 'Test Destination')
        self.assertEqual(destination.country, 'Test Country')
        self.assertEqual(destination.description, 'Test Description')
        self.assertEqual(destination.best_time_to_visit, 'Test Time')
        self.assertEqual(destination.category, 'Beach')
        self.assertEqual(destination.image_url, 'https://example.com/image.jpg')



#integration testing

class DestinationAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_destination(self):
        url = '/api/destinations/'
        data = {
            'name': 'Test Destination',
            'country': 'Test Country',
            'description': 'Test Description',
            'best_time_to_visit': 'Test Time',
            'category': 'Beach',
            'image_url': 'https://example.com/image.jpg'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_destination_list(self):
        url = '/api/destinations/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_destination_detail(self):
        destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Beach',
            image_url='https://example.com/image.jpg'
        )
        url = f'/api/destinations/{destination.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_destination(self):
        destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Beach',
            image_url='https://example.com/image.jpg'
        )
        url = f'/api/destinations/{destination.id}/'
        data = {
            'name': 'Updated Destination Name'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_destination(self):
        destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Beach',
            image_url='https://example.com/image.jpg'
        )
        url = f'/api/destinations/{destination.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
