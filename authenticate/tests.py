from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(username=self.username, password=self.password)
    
    def test_authenticate_user(self):
        login_url = reverse('authenticate:login')
        response = self.client.post(login_url, {'username': self.username, 'password': self.password})

        self.assertEqual(response.status_code, 302)

        user_authenticated = '_auth_user_id' in self.client.session
        self.assertTrue(user_authenticated)

    def test_authenticated_access(self):
        self.client.login(username=self.username, password=self.password)

        url = reverse('stack:ask')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_access(self):
        url = reverse('stack:ask')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
