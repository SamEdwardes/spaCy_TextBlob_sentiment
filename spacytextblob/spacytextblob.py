from typing import Optional, Callable
from spacy.tokens import Doc, Span, Token
from spacy.language import Language

from textblob import TextBlob


@Language.factory("spacytextblob", default_config={"pos_tagger": None, "analyzer": None})
class SpacyTextBlob(object):
    """A spacy pipeline object for sentiment analysis."""
    
    def __init__(self, nlp, name, pos_tagger: Optional[Callable], analyzer: Optional[Callable]):
        # Register custom extensions
        extensions = ["polarity", "subjectivity", "assessments"]
        getters = [self.get_polarity, self.get_subjectivity, self.get_assessments]
        for ext, get in zip(extensions, getters):
            if not Doc.has_extension(ext):
                Doc.set_extension(ext, default=None)
            if not Span.has_extension(ext):
                Span.set_extension(ext, getter=get)
            if not Token.has_extension(ext):
                Token.set_extension(ext, getter=get)

        # Set class attributes
        self.pos_tagger = pos_tagger
        self.analyzer = analyzer

    def __call__(self, doc):
        # Sentiment at the doc level
        sentiment = self.get_sentiment(doc)
        doc._.set("polarity", sentiment.polarity)
        doc._.set("subjectivity", sentiment.subjectivity)
        doc._.set("assessments", sentiment.assessments)
        
        return doc
            
    def get_sentiment(self, doc):
        kwargs = {
            "pos_tagger", self.pos_tagger, 
            "analyzer", self.analyzer
        }
        
        # Only keeps the kwargs that are note note.
        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        blob = TextBlob(doc.text, **kwargs)
        sentiment = blob.sentiment_assessments
        return sentiment
    
    def get_polarity(self, doc):
        return self.get_sentiment(doc).polarity
    
    def get_subjectivity(self, doc):
        return self.get_sentiment(doc).subjectivity
    
    def get_assessments(self, doc):
        return self.get_sentiment(doc).assessments
