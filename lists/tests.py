from urllib import request, response
from django.http import HttpResponse
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
        request = HttpResponse()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
