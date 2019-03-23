import urllib.parse
import urlfetch


class Translate:
    sourceLang = 'auto'
    targetLang = 'he'  # Can Change The target lang here

    def translate(self, quote_str):
        """

        :param quote_str:
        :return:
        """
        url = "https://translate.googleapis.com/" \
              "translate_a/single?client=gtx&sl="\
            + self.sourceLang + "&tl=" + self.targetLang \
              + "&dt=t&q=" + urllib.parse.quote(quote_str.encode('utf-8'))
        result = urlfetch.fetch(url).content.decode('UTF-8')
        strs = result.replace('[', '').split('],')
        print(strs[1])
        return result
