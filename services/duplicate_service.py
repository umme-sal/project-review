from ml.duplicate.duplicate_detector import detector


class DuplicateService:

    def search(self, text):

        return detector.search(text)