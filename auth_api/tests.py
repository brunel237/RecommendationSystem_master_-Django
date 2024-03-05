from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from users_api.models import *

class AuthenticationAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            phone_number='123456789',
            first_name='test',
            last_name='user',
            date_of_birth='2000-02-01',
            sex='male',
            status='student',
            
        )

    # def test_login(self):
    #     url = reverse('login')
    #     data = {
    #         'username': 'testuser',
    #         'password': 'testpassword'
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('token', response.data)

    # def test_logout(self):
    #     url = reverse('logout')
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_register(self):
        url = reverse('signup')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    # def test_change_password(self):
    #     self.client.force_authenticate(user=self.user)
    #     url = reverse('change_password')
    #     data = {
    #         'old_password': 'testpassword',
    #         'new_password': 'newpassword'
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_reset_password(self):
    #     url = reverse('reset_password')
    #     data = {
    #         'email': 'test@example.com'
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
