from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import My_tutorial

class TutorialTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_my_tutorial = My_tutorial.objects.create(
            author = testuser1,
            title = 'Green Eggs and Ham',
            body = 'I do not like green eggs and ham, Sam I  am.'
        )
        test_my_tutorial.save()

    def test_my_tutorial_content(self):
        my_tutorial = My_tutorial.objects.get(id=1)
        actual_author = str(my_tutorial.author)
        actual_title = str(my_tutorial.title)
        actual_body = str(my_tutorial.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'Green Eggs and Ham')
        self.assertEqual(actual_body, 'I do not like green eggs and ham, Sam I  am.')