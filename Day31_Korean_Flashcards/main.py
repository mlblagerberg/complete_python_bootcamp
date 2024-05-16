"""Project: Korean Flashcards
Start: May 16th, 2024
Last touched: May 16th, 2024
Author: Madeleine L.
"""


import pandas as pd

# words = pd.read_excel("한국어 학습용 어휘 목록.xls")
words = pd.read_csv("한국어 학습용 어휘 목록 - 한국어학습용어휘등급표 원어 정보 정리 쿼리.csv")
sorted_words = words.sort_values("순위 (ranking)")
cleaned_words = sorted_words.drop(labels=["품사 (Part of speech)", "단어 (word)", "풀이 (Explanation)", "등급 (Rating)",
                                          "suffix number"], axis=1)
print(cleaned_words.head())
