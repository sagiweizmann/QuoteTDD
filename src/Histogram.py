class Histogram:
    @staticmethod
    def word_counter(quote_str):
        """

        :return:
        :param quote_str:
        :return:
        """
        translate = quote_str.maketrans({char: None for char in "'.,:*!"})
        cleaned_words = quote_str.lower().translate(translate).split()
        word_counter = {}
        for word in cleaned_words:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        return word_counter

    def ret_sorted(self, quote_str):
        """

        :param quote_str:
        """
        word_dict = self.word_counter(quote_str)
        items = word_dict.items()
        after_sort = sorted(items, key=lambda kv: kv[1], reverse=True)
        return after_sort

    @staticmethod
    def print_dict(histogram_dict):
        for k, v in histogram_dict:
            print(k, ', ' + str(v))
