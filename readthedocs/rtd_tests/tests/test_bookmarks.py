from django.contrib.auth.models import User
from django.test import TestCase

from projects.models import Project
from rtd_tests.base import RTDTestCase

# from rtd_tests.utils import make_test_git, make_test_hg


class TestBookmarks(TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_bomb_intentionally(self):
            self.fail("Bombed intentionally!")
