from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='mwibutsa@flor.com', password='password1'):
    """ Create a sample user. """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """ Test Core models. """

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful. """

        email = 'testemail@host.com'
        password = 'TestPassword@132'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tes if the email for a new user is normalized. """

        email = 'test@MWIBUTSA.COM'

        user = get_user_model().objects.create_user(
            email=email, password='test_123'
        )

        self.assertEqual(user.email, email.lower())

    def test_create_user_invalid_email(self):
        """ test creating user with no email raises error. """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                'any_password'
            )

    def test_create_super_user(self):
        """ Tests creating a new super user. """

        user = get_user_model().objects.create_superuser(
            email='superuseremail@gmail.com',
            password='FPassword'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Test the tag string representation. """

        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """ Test ingredient strig representation. """

        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
