from src.Quote import Quote
from src.Histogram import Histogram
from src.Translate import Translate


quote_obj = Quote()
histogram_obj = Histogram()
translate_obj = Translate()
quote = quote_obj.get_quote()
print(quote)
print(translate_obj.translate(quote))
histogram_obj.print_sorted(quote)
