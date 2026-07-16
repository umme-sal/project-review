from ml.inference.summarizer import summarizer


class SummaryService:

    def summarize(self, text):

        return summarizer.summarize(text)