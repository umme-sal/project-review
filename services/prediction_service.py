from ml.inference.classifier import classifier


class PredictionService:

    def predict(self, text: str):

        return classifier.predict(text)