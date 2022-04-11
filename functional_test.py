from email import header
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self) -> None:
        self.browser.quit()
    
    def test_add_item_and_retrieve_later(self):
        """ToDo List in title and header"""
        self.browser.get('http://localhost:8000/')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header.text)

        """Add "buy feather" as item"""
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter To-Do item')

        inputbox.send_keys('Buy feather')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy feather' for row in rows))

        # There is still a textbox to add another "fly home" item

    
        """after adding, see a personal url and check that to-do is still there"""

        self.fail('finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')