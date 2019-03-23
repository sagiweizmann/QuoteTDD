import unittest
from src.Quote import Quote
from src.Histogram import Histogram
from mock import patch
import json


class HistogramTest(unittest.TestCase):
    @patch('Quote.get_quote_as_dict')
    def test1(self, mock_quote):
        mock_quote = Quote()
        with open("../mockquote/mockqoute1.json") as f:
            mock_quote.get_quote_as_dict.return_value = json.load(f)
        quote = mock_quote.get_quote()
        self.assertEqual(4, 4, quote)

    def test2(self):
        pass
