
try:
    import spacy
    from spacytextblob.spacytextblob import SpacyTextBlob

except Exception as e:
    print('#!pip3 install spacy[transformers] torch spacytextblob')
    print('#!python3 -m spacy download en_core_web_sm')
    raise e


class SentimentAnalyserClass():
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.nlp.add_pipe("spacytextblob")
        
    def predict(self,text):
        if (type(text) == list):
            print("This is a list")
            doc = [self.nlp(t) for t in text]
            sentiments = [d._.blob.sentiment for d in doc]
            assessments = [d._.blob.sentiment_assessments for d in doc]
            tags = [d._.blob.tags for d in doc]
            phrases=[d._.blob.noun_phrases for d in doc]
        else:
            print("This is a string")
            doc = self.nlp(text)
            sentiments = doc._.blob.sentiment #_assessments.assessments
            assessments = doc._.blob.sentiment_assessments
            tags = doc._.blob.tags
            phrases = doc._.blob.noun_phrases
        return sentiments, assessments, tags, phrases
    
    def test(self):
        print("#TODO")
        raise
        #text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."