import unittest
from src.Quote import Quote
from src.Histogram import Histogram
from mock import patch, call
import json
import operator


class HistogramTest(unittest.TestCase):
    @patch('src.Quote.Quote.get_quote_as_dict')
    def test1(self, func_quote):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        histogram_obj = Histogram()
        histogram_dict = histogram_obj.word_counter(quote)
        assert histogram_dict['it'] == 5

    @patch('src.Quote.Quote.get_quote_as_dict')
    def test2(self, func_quote):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        histogram_obj = Histogram()
        histogram_dict = histogram_obj.word_counter(quote)
        assert histogram_dict['dont'] == 3

    @patch('src.Quote.Quote.get_quote_as_dict')
    def test3(self, func_quote):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        histogram_obj = Histogram()
        histogram_dict = histogram_obj.word_counter(quote)
        items = histogram_dict.items()
        max_dict = max(items, key=operator.itemgetter(1))[0]
        assert max_dict == 'it'

    @patch('src.Quote.Quote.get_quote_as_dict')
    def test4(self, func_quote):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        histogram_obj = Histogram()
        histogram_dict = histogram_obj.word_counter(quote)
        assert histogram_dict['buy'] == 2

    @patch('src.Quote.Quote.get_quote_as_dict')
    def test5(self, func_quote):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        histogram_obj = Histogram()
        histogram_dict = histogram_obj.word_counter(quote)
        items = histogram_dict.items()
        min_dict = min(items, key=operator.itemgetter(1))[0]
        assert min_dict == 'gamble;'
