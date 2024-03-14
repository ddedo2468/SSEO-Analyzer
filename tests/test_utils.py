import unittest
from unittest.mock import patch, MagicMock
from app import app
from app.utlis import get_soup, analyze_url, analyze_head, analyze_body, analyze_h_tags_order, get_keywords
import requests
from bs4 import BeautifulSoup


class TestUtils(unittest.TestCase):

    @patch('requests.get')
    def test_get_soup_valid_url(self, mock_get):
        """Tests get_soup with a valid URL, ensuring BeautifulSoup object is returned."""
        mock_response = MagicMock()
        mock_response.content = b'<html><head><title>Test Title</title></head></html>'
        mock_get.return_value = mock_response

        url = 'https://en.wikipedia.org/wiki/Cat'
        soup = get_soup(url)

        self.assertIsInstance(soup, BeautifulSoup)
        self.assertEqual(soup.title.text, 'Test Title')

    @patch('requests.get')
    def test_get_soup_invalid_url(self, mock_get):
        """Tests get_soup with an invalid URL, raising requests.exceptions.RequestException."""
        mock_get.side_effect = requests.exceptions.RequestException

        url = 'invalid_url'

        with self.assertRaises(requests.exceptions.RequestException):
            get_soup(url)

    def test_analyze_head_with_title_and_description(self):
        """Tests analyze_head with a soup containing title and description meta tags."""
        soup = BeautifulSoup('<html><head><title>Test Title</title><meta name="description" content="A test description"></head></html>', 'html.parser')

        results = analyze_head(soup)

        self.assertEqual(results['title'], 1)
        self.assertEqual(results['title_length'], 10)
        self.assertEqual(results['description'], 1)

    def test_analyze_head_without_title(self):
        """Tests analyze_head with a soup mising the title tag."""
        soup = BeautifulSoup('<html><head><meta name="description" content="A test description"></head></html>', 'html.parser')

        results = analyze_head(soup)

        self.assertEqual(results['title'], 0)
        self.assertEqual(results['title_length'], 0)
        self.assertEqual(results['description'], 1)

    def test_analyze_head_without_description(self):
        """Tests analyze_head with a soup missing the description meta tag."""
        soup = BeautifulSoup('<html><head><title>Test Title</title></head></html>', 'html.parser')

        results = analyze_head(soup)

        self.assertEqual(results['title'], 1)
        self.assertEqual(results['title_length'], 10)
        self.assertEqual(results['description'], 0)

    def test_analyze_h_tags_order_valid(self):
        """Tests analyze_h_tags_order with headings in correct order (H1, H2, H3)."""
        soup = BeautifulSoup('<h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3>', 'html.parser')

        result = analyze_h_tags_order(soup)

        self.assertEqual(result, 1)

    def test_analyze_h_tags_order_invalid(self):
        """Tests analyze_h_tags_order with headings in incorrect order (H2, H1)."""
        soup = BeautifulSoup('<h2>Heading 2</h2><h1>Heading 1</h1>', 'html.parser')

        result = analyze_h_tags_order(soup)

        self.assertEqual(result, 0)

    @patch('nltk.FreqDist')
    @patch('nltk.corpus.stopwords.words')
    def test_get_keywords(self, mock_stopwords, mock_freqdist):
        """Tests get_keywords with a mock stopwords list and bigram frequency distribution."""
        body_text = "This is a test document about natural language processing."
        soup = BeautifulSoup(f'<html><body>{body_text}</body></html>', 'html.parser')

        mock_stopwords.return_value = ['is', 'a', 'the']
        mock_freqdist.return_value.most_common = MagicMock(return_value=[
            (('natural', 'language'), 2),
            (('language', 'processing'), 1)
        ])

        keywords = get_keywords(soup)

        self.assertEqual(keywords, {
            '1': 'natural language',
            '2': 'language processing'
        })

if __name__ == '__main__':
    unittest.main()
