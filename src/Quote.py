import json
import requests


class Quote:
    def __init__(self):
        pass

    @staticmethod
    def get_quote_as_json():
        """

        :return:
        """
        quote_request = requests.get('https://favqs.com/api/qotd')
        return quote_request.json()

    def get_quote_as_dict(self):
        """

        :return: dict
        """
        get_data = self.get_quote_as_json()
        convert = json.dumps(get_data)
        data = json.loads(convert)
        with open("../mockquote/mockqoute1.json") as f:
            data = json.load(f)
        return data

    def get_quote(self):
        """

        :return:
        """
        quote_dict = self.get_quote_as_dict()
        author = quote_dict['quote']['author']
        body = quote_dict['quote']['body']
        quote = body + '\n-' + author
        return quote
