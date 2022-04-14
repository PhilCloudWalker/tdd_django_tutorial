from ast import While
from email import header
from pickle import TRUE
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException

MAX_WAIT = 3

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        start = time.time()

        while TRUE:
            try: 
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start > MAX_WAIT:
                    raise e
                time.sleep(.5)
    
    def test_add_item_and_retrieve_later(self):
        """Check if items can be added and retrieved"""

        #ToDo List in title and header
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        #Add "buy feather" as item
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')


        inputbox.send_keys('Buy feather')
        inputbox.send_keys(Keys.ENTER)
        
        # There is still a textbox to add another "fly home with feather" item
        time.sleep(1)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Fly home with feather')
        inputbox.send_keys(Keys.ENTER)        
        
        # check for correct entries in todo list
        self.check_for_row_in_list_table('1: Buy feather')
        self.check_for_row_in_list_table('2: Fly home with feather')

    def test_multiple_user_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy feather')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy feather')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, 'lists/.+')

        # Now a new user comes

        # Make sure they do not see Ediths Info
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # ensure no info of edith
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy feather', page_text)
        self.assertNotIn('Fly home', page_text)

        # Francis starts a new list
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        # Francis get own url
        francis_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, 'lists/.+')
        self.assertNotEqual(edith_list_url, francis_list_url)

        # Again, no trace of edith
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy feather', page_text)
        self.assertIn('Buy milk', page_text)


    def test_layout_and_styling(self):
        # smoke test for the layout

        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2, 512, delta=10)

        # Edith starts a new list and sees the nicely centered inputbox
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2, 512, delta=10)
        





if __name__ == '__main__':
    unittest.main(warnings='ignore')