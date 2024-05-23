from django.test import TestCase
from .models import Destination
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from rest_framework import status


#unit testing
class DestinationModelTestCase(TestCase):
    def test_destination_fields(self):
        destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Test Category',
            image_url='http://example.com/test.jpg'
        )
        self.assertEqual(destination.name, 'Test Destination')
        self.assertEqual(destination.country, 'Test Country')
        self.assertEqual(destination.description, 'Test Description')
        self.assertEqual(destination.best_time_to_visit, 'Test Time')
        self.assertEqual(destination.category, 'Test Category')
        self.assertEqual(destination.image_url, 'http://example.com/test.jpg')

    def test_destination_constraints(self):
        max_length_name = Destination._meta.get_field('name').max_length

        valid_name = 'x' * max_length_name
        destination = Destination(
            name=valid_name,
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Anytime',
            category='Beach',
            image_url='http://example.com/test.jpg'
        )
        try:
            destination.full_clean() 
        except ValidationError:
            self.fail('Destination with valid name length should not raise ValidationError')

        invalid_name = 'x' * (max_length_name + 1)
        destination = Destination(
            name=invalid_name,
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Anytime',
            category='Beach',
            image_url='http://example.com/test.jpg'
        )
        with self.assertRaises(ValidationError):
            destination.full_clean() 
            
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
