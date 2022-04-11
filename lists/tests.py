from urllib import request, response
from django.http import HttpRequest, HttpResponse
from django.urls  import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpResponse
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    def test_root_url_goes_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_view_return_correct_values(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_homepage_can_save_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
