
try:
    from googletrans import Translator
except Exception as e:
    print('#!pip install googletrans')
    raise e
from pprint import pprint


class TranslatorClass():
    def __init__(self):
        # init the Google API translator
        self.translator = Translator()
        #self.test()
        
    def translate(self, text, PRINT=False, EXTRA=False):
        translation = self.translator.translate(text, src="fi", dest="en")
        if (type(text) == list):
            return [t.text for t in translation]
        else:
            if PRINT:
                print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
            if EXTRA:
                pprint(translation.extra_data)
            return translation.text
        
    def test(self):
        assert ((self.translate("Hei")) == "Hey")
    
