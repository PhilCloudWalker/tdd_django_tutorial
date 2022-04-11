from unicodedata import name
from selenium import webdriver
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

        """Add "buy feather" and "make a fly" to as items"""

    
        """after adding, see a personal url and check that to-do is still there"""

        self.fail('finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')