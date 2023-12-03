import unittest
import web_scraper

class Test_Web_Scraper(unittest.TestCase):
    def test_recursive_call(self):

        unique_url = {"https://apple.com"}
        web_scraper.web_crawler(unique_url)


if __name__ == '__main__':
    unittest.main()
