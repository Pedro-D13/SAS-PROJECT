from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from .views import PostCreateView
from blog.models import Post
# Create your tests here


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="UTest",
                                             email='fake@something.com',
                                             password="secretpass")
        self.post = Post.objects.create(title="Test case example",
                                        content="testing",
                                        author=self.user)
        self.post.save()
        self.newest_post = Post.objects.latest('date_posted')

    def test_created(self):
        newest_post = Post.objects.latest('date_posted')
        self.assertEqual(newest_post.title, 'Test case example')

    def 

