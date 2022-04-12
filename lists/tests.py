from urllib import request, response
from django.http import HttpRequest, HttpResponse
from django.urls  import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpResponse
from django.template.loader import render_to_string

from lists.models import Item, List


class HomePageTest(TestCase):

    def test_root_url_goes_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_view_return_correct_values(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class ListandItemModelTest(TestCase):

    def test_saving_and_retrieving_item(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'The 2nd item'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'The 2nd item')
        self.assertEqual(second_saved_item.list, list_)

class ListViewTest(TestCase):

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='item1', list=list_)
        Item.objects.create(text='item2', list=list_)

        response = self.client.get(f'/lists/{list_.id}/')

        self.assertContains(response, 'item1')
        self.assertContains(response, 'item2')

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_display_only_items_for_that_list(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        item1_list1 = Item.objects.create(text='1st item list 1', list=list1)
        item2_list1 = Item.objects.create(text='2nd item list 1', list=list1)
        item1_list2 = Item.objects.create(text='1st item list 2', list=list2)

        response = self.client.get(f'/lists/{list1.id}/')

        self.assertContains(response, '1st item list 1')
        self.assertContains(response, '2nd item list 1')
        self.assertNotContains(response, '1st item list 2')
    
    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.get(f'/lists/{correct_list.id}/')

        self.assertEqual(response.context['list'], correct_list)


class NewListTest(TestCase):

    def test_homepage_can_save_post_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
    
    def test_redirect_after_post(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        new_list = List.objects.first()        
        self.assertRedirects(response, f'/lists/{new_list.id}/') 

class NewItemTest(TestCase):

    def test_add_item_to_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new item to existing list'})
        
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item to existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirect_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new item to existing list'})

        self.assertRedirects(response, f'/lists/{correct_list.id}/')


