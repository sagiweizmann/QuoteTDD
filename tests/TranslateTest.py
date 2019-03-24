import unittest
from src.Quote import Quote
from src.Translate import Translate
from mock import patch
import json


class TranslateTest(unittest.TestCase):
    @patch('src.Quote.Quote.get_quote_as_dict')
    @patch('src.Translate.Translate.translate')
    def test1(self, func_quote, translate_func):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("/home/semaphore/QuoteTDD/tests/mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        translate_obj = Translate()
        translate_obj.translate = translate_func
        with open("/home/semaphore/QuoteTDD/tests/mocktranslate.txt",encoding="utf8") as f2:
            translate_obj.translate.return_value = f2.read()
        result = translate_obj.translate(quote)
        strs = result.replace('[', '').split('],')
        assert strs[0].find('להמר') != -1

    @patch('src.Quote.Quote.get_quote_as_dict')
    @patch('src.Translate.Translate.translate')
    def test2(self, func_quote, translate_func):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("/home/semaphore/QuoteTDD/tests/mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        translate_obj = Translate()
        translate_obj.translate = translate_func
        with open("/home/semaphore/QuoteTDD/tests/mocktranslate.txt",encoding="utf8") as f2:
            translate_obj.translate.return_value = f2.read()
        result = translate_obj.translate(quote)
        strs = result.replace('[', '').split('],')
        assert strs[0].find('לא') != -1

    @patch('src.Quote.Quote.get_quote_as_dict')
    @patch('src.Translate.Translate.translate')
    def test3(self, func_quote, translate_func):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("/home/semaphore/QuoteTDD/tests/mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        translate_obj = Translate()
        translate_obj.translate = translate_func
        with open("/home/semaphore/QuoteTDD/tests/mocktranslate.txt",encoding="utf8") as f2:
            translate_obj.translate.return_value = f2.read()
        result = translate_obj.translate(quote)
        strs = result.replace('[', '').split('],')
        assert strs[1].find('החסכונות') != -1

    @patch('src.Quote.Quote.get_quote_as_dict')
    @patch('src.Translate.Translate.translate')
    def test4(self, func_quote, translate_func):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("/home/semaphore/QuoteTDD/tests/mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        translate_obj = Translate()
        translate_obj.translate = translate_func
        with open("/home/semaphore/QuoteTDD/tests/mocktranslate.txt",encoding="utf8") as f2:
            translate_obj.translate.return_value = f2.read()
        result = translate_obj.translate(quote)
        strs = result.replace('[', '').split('],')
        assert strs[3].find("רוג'רס") != -1

    @patch('src.Quote.Quote.get_quote_as_dict')
    @patch('src.Translate.Translate.translate')
    def test5(self, func_quote, translate_func):
        quote_obj = Quote()
        quote_obj.get_quote_as_dict = func_quote
        with open("/home/semaphore/QuoteTDD/tests/mockqoute1.json") as f:
            quote_obj.get_quote_as_dict.return_value = json.load(f)
        quote = quote_obj.get_quote()
        translate_obj = Translate()
        translate_obj.translate = translate_func
        with open("/home/semaphore/QuoteTDD/tests/mocktranslate.txt",encoding="utf8") as f2:
            translate_obj.translate.return_value = f2.read()
        result = translate_obj.translate(quote)
        strs = result.replace('[', '').split('],')
        assert strs[1].find('מלאי טוב') != -1

