"""Project: Korean Flashcards
Start: May 16th, 2024
Last touched: May 16th, 2024
Author: Madeleine L.
"""


import pandas as pd

words = pd.read_excel("한국어 학습용 어휘 목록.xls")
sorted_words = words.sort_values("순위")
print(sorted_words.head())
