from ml.inference.priority import priority_classifier


class PriorityService:

    @staticmethod
    def predict(text):

        return priority_classifier.predict(text)