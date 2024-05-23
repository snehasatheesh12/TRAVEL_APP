from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Destination
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class DestinationModelTestCase(TestCase):
    def test_destination_name_max_length(self):
        max_length_name = Destination._meta.get_field('name').max_length
        test_name = 'x' * max_length_name
        destination = Destination.objects.create(
            name=test_name,
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Anytime',
            category='Beach',
            image_url='http://example.com/test.jpg'
        )
        self.assertEqual(len(destination.name), max_length_name)



class DestinationModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.destination = Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Anytime',
            category='Beach',
            image_url='http://example.com/test.jpg'
        )

    def test_destination_name(self):
        self.assertEqual(self.destination.name, 'Test Destination')

    def test_destination_country(self):
        self.assertEqual(self.destination.country, 'Test Country')

    def test_destination_description(self):
        self.assertEqual(self.destination.description, 'Test Description')

    def test_destination_best_time_to_visit(self):
        self.assertEqual(self.destination.best_time_to_visit, 'Anytime')

    def test_destination_category(self):
        self.assertEqual(self.destination.category, 'Beach')

    def test_destination_image_url(self):
        self.assertEqual(self.destination.image_url, 'http://example.com/test.jpg')

    def test_str_representation(self):
        expected_str = 'Test Destination'
        self.assertEqual(str(self.destination), expected_str)

