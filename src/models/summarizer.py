from transformers import pipeline
import time as time


class Summarizer:
    """
    Решает задачу саммаризации
    """

    def summarize(self, text: str):
        start = time.time()
        print(f'summarizer started')

        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        model_result = summarizer(
            text,
            do_sample=False)
        result = model_result[0]['summary_text']

        end = time.time()
        print(f'summarizer finished, elapsed {end - start} sec')
        return result