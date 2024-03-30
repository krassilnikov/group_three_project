from src.models.summarizer import Summarizer
from src.models.summarizer_spacy import SummarizerSpacy
from src.models.translator import Translator


class TextSummaryService():
    """
    Оркестратор пайплайна суммаризации
    """

    def __init__(self):
        self.translator = Translator()
        self.summarizer = Summarizer()
        self.summarizer_spacy = SummarizerSpacy()

    def handle(self, text: str, useV2: bool):
        if useV2:
            return self.summarizer_spacy.summarize(text)
        else:
            enText = self.translator.ru_en(text)
            original_summary = self.summarizer.summarize(enText)
            ruSummary = self.translator.en_ru(original_summary)
            return ruSummary