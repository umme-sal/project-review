from transformers import pipeline


class SentimentClassifier:

    def __init__(self):

        self.pipeline = pipeline(

            task="sentiment-analysis",

            model="distilbert-base-uncased-finetuned-sst-2-english"

        )

    def predict(self, text):

        result = self.pipeline(text)[0]

        return {

            "sentiment": result["label"],

            "confidence": round(result["score"], 4)

        }


sentiment_classifier = SentimentClassifier()