# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:35:55 2021

@author: TanayGupta
"""

import nltk
nltk.download('punkt')
import urllib
import bs4 as bs
import re

from nltk.corpus import stopwords
nltk.download('stopwords')

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Climate_change').read()

soup = bs.BeautifulSoup(source, 'lxml')

text= ""

for paragraph in soup.find_all('p'):
    text +=paragraph.text
    
    

text = re.sub(r'\[[0-9]*\]', ' ',text)
text = re.sub(r'\s+', ' ', text)
text = text.lower()
text = re.sub(r'\d',' ', text)
text = re.sub(r'\s+', ' ', text)


sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
