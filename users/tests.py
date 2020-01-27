from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username='sam',
            email='sam@gmail.com',
            password='testpass123'
        )

        self.assertEqual(user.username, 'sam')
        self.assertEqual(user.email,'sam@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    

    def test_create_superuser(self):
        User = get_user_model()
        superUser = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='testpass123'
        )

        self.assertEqual(superUser.username, 'admin')
        self.assertEqual(superUser.email,'admin@test.com')
        self.assertTrue(superUser.is_active)
        self.assertTrue(superUser.is_staff)
        self.assertTrue(superUser.is_superuser)
