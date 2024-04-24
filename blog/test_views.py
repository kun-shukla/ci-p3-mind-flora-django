from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm, ShareDiscoveryForm
from .models import Post, About, AboutSectionNavImage

class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(category="0", title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

        self.about = About(title="About title", content="About content")
        self.about.save()

        self.aboutNav = AboutSectionNavImage(title="About navigation title")
        self.aboutNav.save()

    def test_render_post_detail_page_with_comment_form(self):
        """Verifies get request for 'post detail' page containing a comment form"""
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_render_index_page_with_share_a_discovery_form(self):
        """Verifies get request for index page containing a 'Share a Discovery' form"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Blog title', response.content)
        self.assertIn(b'About title', response.content)
        self.assertIn(b'About navigation title', response.content)
        self.assertIsInstance(response.context['share_form'], ShareDiscoveryForm)

