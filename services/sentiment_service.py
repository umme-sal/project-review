from ml.inference.sentiment import sentiment_classifier


class SentimentService:

    def predict(self, text):

        return sentiment_classifier.predict(text)