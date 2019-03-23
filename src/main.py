from src.Quote import Quote
from src.Histogram import Histogram
from src.Translate import Translate


QUOTE_OBJ = Quote()
HISTOGRAM_OBJ = Histogram()
TRANSLATE_OBJ = Translate()
QUOTE = QUOTE_OBJ.get_quote()
print(QUOTE)
print(TRANSLATE_OBJ.translate(QUOTE))
HISTOGRAM_OBJ.print_sorted(QUOTE)
