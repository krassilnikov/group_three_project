from transformers import pipeline
import time as time


class Translator:
    """
    Перевод текста
    ru-en
    en-ru
    """

    def ru_en(self, text: str):
        model = pipeline("translation", 'Helsinki-NLP/opus-mt-ru-en')
        rslt = model(text)[0]['translation_text']
        return rslt

    def en_ru(self, text: str):
        model = pipeline("translation", 'Helsinki-NLP/opus-mt-en-ru')
        rslt = model(text)[0]['translation_text']
        return rslt