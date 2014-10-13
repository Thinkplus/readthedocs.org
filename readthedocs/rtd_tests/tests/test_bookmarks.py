# import json

from django.test import TestCase
from bookmarks.models import Bookmark

class TestBookmarks(TestCase):

    def setUp(self):
        self.client.login(username = 'eric', password='test')

    def tearDown(self):
        pass

    def test_bookmark_index_list(self):
        response = self.client.get('/bookmarks/')
        self.assertEqual(response.status_code, 200)


# def bookmark_list(request, queryset=Bookmark.objects.all()):
# >>> from django.test.client import Client
# >>> c = Client()
# >>> response = c.post('/login/', {'username': 'john', 'password': 'smith'})
# >>> response.status_code
# 200
# >>> response = c.get('/customer/details/')
# >>> response.content
