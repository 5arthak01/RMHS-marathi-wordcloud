import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from cltk.corpus.marathi.alphabet import (
    VOWELS,
    SEMI_VOWELS,
    VELAR_CONSONANTS,
    PALATAL_CONSONANTS,
    RETROFLEX_CONSONANTS,
    DENTAL_CONSONANTS,
    LABIAL_CONSONANTS,
    ADDITIONAL_CONSONANTS,
    FRIACTIVE_CONSONANTS,
    SIBILANTS,
    DIGITS,
)

STOP_LIST = [
    "न",
    "तरी",
    "तो",
    "हें",
    "तें",
    "कां",
    "आणि",
    "जें",
    "जे",
    "मग",
    "ते",
    "मी",
    "जो",
    "परी",
    "गा",
    "हे",
    "ऐसें",
    "आतां",
    "तैसें",
    "परि",
    "नाहीं",
    "तेथ",
    "हा",
    "तया",
    "असे",
    "म्हणे",
    "काय",
    "म्हणौनि",
    "कीं",
    "जैसें",
    "तंव",
    "तूं",
    "होय",
    "जैसा",
    "आहे",
    "पैं",
    "तैसा",
    "जरी",
    "म्हणोनि",
    "एक",
    "ऐसा",
    "जी",
    "ना",
    "मज",
    "एथ",
    "या",
    "जेथ",
    "जया",
    "तुज",
    "तेणें",
    "तैं",
    "पां",
    "असो",
    "करी",
    "ऐसी",
    "येणें",
    "जाहला",
    "तेंचि",
    "आघवें",
    "होती",
    "जैं",
    "कांहीं",
    "होऊनि",
    "एकें",
    "मातें",
    "ठायीं",
    "ये",
    "अर्जुना",
    "सकळ",
    "केलें",
    "जेणें",
    "जाण",
    "जैसी",
    "होये",
    "जेवीं",
    "एऱ्हवीं",
    "मीचि",
    "किरीटी",
    "दिसे",
    "देवा",
    "हो",
    "तरि",
    "कीजे",
    "तैसे",
    "आपण",
    "तिये",
    "कर्म",
    "नोहे",
    "इये",
    "पडे",
    "पार्था",
    "माझें",
    "तैसी",
    "लागे",
    "नाना",
    "जंव",
    "कीर",
]

ALPHABET = (
    VOWELS
    + SEMI_VOWELS
    + VELAR_CONSONANTS
    + PALATAL_CONSONANTS
    + RETROFLEX_CONSONANTS
    + DENTAL_CONSONANTS
    + LABIAL_CONSONANTS
    + ADDITIONAL_CONSONANTS
    + FRIACTIVE_CONSONANTS
    + SIBILANTS
    + DIGITS
)

stpwrds = []
with open("marathi_stopwords.txt", "r", encoding="utf-8") as f:
    stpwrds = f.readlines()
stopwords = set(STOP_LIST + [x.strip(" \n") for x in stpwrds] + ALPHABET)

words = ""
with open("./loksatta/all_loksatta_articles.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter="|")
    count = 0
    for article in spamreader:
        words += article[-1] + " "
words = words.replace("  ", " ")

wordcloud = WordCloud(
    font_path="Lohit-Marathi.ttf",
    width=800,
    height=800,
    background_color="white",
    stopwords=stopwords,
    min_font_size=10,
    regexp=r"[\u0900-\u097F]+",
).generate(words)
wordcloud.to_file("loksatta_wordcloud.png")

# # plot the WordCloud image
# plt.figure(figsize=(8, 8), facecolor=None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad=0)

# plt.show()
