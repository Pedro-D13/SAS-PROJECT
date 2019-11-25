from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post


class PostTestCase(TestCase):
    ''' this class sets up a new user,with credientials, and creates a post using that user'''

    def setUp(self):
        ''' initial setUp method'''
        self.user = User.objects.create_user(
            username="UTest", email='fake@something.com', password="secretpass")

        self.post = Post.objects.create(
            title="Test case example", content="testing", author=self.user)
        self.post.save()
        self.newest_post = Post.objects.latest('date_posted')

    def test_created(self):
        ''' Tests to see if the posts that's recently created is from that user'''
        newest_post = Post.objects.latest('date_posted')
        self.assertEqual(newest_post.title, 'Test case example')


# Tests to write:
''' 
#1  Ensure that the user gets assigned a profile once they create an account 
#2  
#3

'''
