from transformers import pipeline


class TicketSummarizer:

    def __init__(self):

        self.model = pipeline(

            task="summarization",

            model="facebook/bart-large-cnn"

        )

    def summarize(self, text):

        if len(text.split()) < 40:
            return {
                "summary": text
            }

        summary = self.model(
            text,
            max_length=60,
            min_length=20,
            do_sample=False
        )

        return {
            "summary": summary[0]["summary_text"]
        }


summarizer = TicketSummarizer()