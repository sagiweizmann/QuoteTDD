class Histogram:
    @staticmethod
    def word_counter(quote_str):
        translate = quote_str.maketrans({char: None for char in "'.,:*!"})
        cleaned_words = quote_str.lower().translate(translate).split()
        word_counter = {}
        for word in cleaned_words:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        return word_counter

    def print_sorted(self, quote_str):
        word_counter_dict = self.word_counter(quote_str)
        for k, v in sorted(word_counter_dict.items(),  key=lambda kv: kv[1], reverse=True):
            print(k, ', ' + str(v))
