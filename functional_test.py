from email import header
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_add_item_and_retrieve_later(self):
        """ToDo List in title and header"""
        self.browser.get('http://localhost:8000/')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        """Add "buy feather" as item"""
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter To-Do item')

        inputbox.send_keys('Buy feather')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(5)
        

        # There is still a textbox to add another "fly home" item
        self.check_for_row_in_list_table('1: Buy feather')

    
        """after adding, see a personal url and check that to-do is still there"""

        self.fail('finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')