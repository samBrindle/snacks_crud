from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.

class SnackTests(TestCase):
    def create(self):
        self.user = get_user_model().objects.create_user(
            username="test", email="test@gmail.com", password="testing",
        )
        self.snack = Snack.objects.create(
            title="oreo", description="chocolate cookie", purchaser=self.user,
        )

    def test_string(self):
        self.assertEqual(str(self.snack), "oreo")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "oreo")
        self.assertEqual(f"{self.snack.description}", "chocolate cookie")
        self.assertEqual(f"{self.snack.purchaser}", "test")

    def test_snack_list(self):
        response = self.client.get(reverse('snack_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "oreo")
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_detail(self):
        response = self.client.get(reverse('snacl_detail', args='1'))

        self.assertEqual((response.status_code, 200))
        self.assertContains(response, "test")
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_create(self):
        response = self.client.post(
            reverse('snack_create'),{
                "title": "pizza",
                "description": "delicious cheesey food",
                "purchaser": self.user.id
            }, follow=True
        )

        self.assertRedirects(response, reverse('snack_detail', args='2'))
        self.assertContains(response, "pizza")

    def test_snack_delete(self):
        response = self.client.get(reverse('snack_delete', args='1'))
        self.assertEqual(response.status_code, 200)