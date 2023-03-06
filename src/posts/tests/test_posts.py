from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from posts.models import Post
from posts.serializers import PostSerializer


class PostTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_get_all_posts(self):
        response = self.client.get('/posts/')
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_post(self):
        response = self.client.get(f'/posts/{self.post.id}/')
        post = Post.objects.get(pk=self.post.id)
        serializer = PostSerializer(post)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_post(self):
        data = {'title': 'New Post', 'content': 'This is a new post.'}
        response = self.client.post('/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(title=data['title']).content, data['content'])

    def test_update_post(self):
        data = {'title': 'Updated Post', 'content': 'This is an updated post.'}
        response = self.client.put(f'/posts/{self.post.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, data['title'])
        self.assertEqual(self.post.content, data['content'])

    def test_delete_post(self):
        response = self.client.delete(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
