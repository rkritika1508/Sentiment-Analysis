# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:44:47 2019

@author: dell
"""

import html
import re
from nltk.tokenize import TreebankWordTokenizer
token = TreebankWordTokenizer()
mentions = r'@[A-Za-z0-9]+'
url_https = 'https?://[A-Za-z0-9./]+'
url_www = r'www.[^ ]+'
negations = {"isn't":"is not", "aren't":"are not", "wasn't":"was not", "weren't":"were not",
             "haven't":"have not","hasn't":"has not","hadn't":"had not","won't":"will not",
             "wouldn't":"would not", "don't":"do not", "doesn't":"does not","didn't":"did not",
             "can't":"can not","couldn't":"could not","shouldn't":"should not","mightn't":"might not",
             "mustn't":"must not"
            }
def tweet_cleaning(text):
    text = html.unescape(text)
    text = re.sub(mentions, '', text)
    text = re.sub(url_https, '', text)
    text = re.sub(url_www, '', text)
    text = re.sub("RT ", "", text)
    text = text.lower()
    for a, b in negations.items():
        if a in text:
            text = text.replace(a,b)
    #Removing characters except letters
    text = re.sub("[^a-zA-Z]", " ", text)
    #Removing unnecessary white spaces using tokenizer
    word_list = token.tokenize(text)
    text = " ".join(word_list).strip()
    return text