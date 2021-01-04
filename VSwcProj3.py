import numpy as np
from os import path
import sys
import wordcloud
import matplotlib.pyplot as plt


def txtfreqdict(sentence):

# Eleminate these list of punctuations and uninteresting words
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

# code to clean-up data
    frequencies = {}
    case = sentence.split()
    for word in case:
        words = word.strip(punctuations)
        lower = words.lower()
        if lower.isalpha() == False or lower in uninteresting_words:
            continue
        elif lower not in frequencies:
            frequencies[lower]= 0
        frequencies[lower]+=1
    return frequencies

def makemywc(frequencies):
    # As required by python project
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    cloud.to_file("myfile.jpg")

    # setup show
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()


# using getcwd() is needed to get data directory
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

frequencies = open(path.join(d, sys.argv[1]), encoding='utf-8')
frequencies = frequencies.read()
makemywc(txtfreqdict(frequencies))