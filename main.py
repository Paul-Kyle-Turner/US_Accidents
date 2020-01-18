import numpy as np
import pandas as pd
import re

import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import preprocess_documents
from gensim.test.utils import get_tmpfile
from gensim.models import Phrases
from gensim.models.phrases import Phraser
from gensim.models import Word2Vec
import gensim.corpora as corpora
from gensim.models.ldamodel import LdaModel
from nltk.corpus import stopwords
import pyLDAvis
import pyLDAvis.gensim
import spacy
import pickle

import matplotlib.pyplot as plt

from sklearn.manifold import TSNE


class RegexReplacer:

    # Simple regex to change the multiple white space issue
    @staticmethod
    def regex_replacer(text, regex=r'\s+', replacement_text=' '):
        reg_text = []
        for desc in text:
            reg_text.append(re.sub(regex, replacement_text, desc))
        return reg_text

    """
    Replaces the regex multiple times, for easy regex use
        Not best practice but easier

        :param
            text - an array type that holds the text that you want to have replacements done on
            regex - an array or dict type object of the regular expression and if dict type object the regular
             expression and replacement text
            replacement_text - array type object only used it the regex object is not dict
    """
    @staticmethod
    def regex_multi_replacer(text, regex, replacement_text=None):
        if type(regex) is dict:
            for key in regex:
                text = RegexReplacer.regex_replacer(text, key, regex[key])
        else:
            for key, value in zip(regex, replacement_text):
                text = RegexReplacer.regex_replacer(text, key, value)
        return text


def create_gensim_word_2_vec_model(content_list):
    gensim_content_list = preprocess_documents(content_list)
    bigrams = Phrases(gensim_content_list)
    word_to_vec_model = Word2Vec(bigrams[gensim_content_list], min_count=1, window=3, size=300)
    return word_to_vec_model


# Author Anthony Breitzman, modifications Paul Turner
# This is used to create a topic model of the given descriptions
def remove_stopwords(texts, stop_words):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]


def sent_to_words(sentences):
    for sentence in sentences:
        yield simple_preprocess(str(sentence), deacc=True)


def make_bigrams(texts, bigram_mod):
    return [bigram_mod[doc] for doc in texts]


def make_trigrams(texts, bigram_mod, trigram_mod):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]


def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    nlp = spacy.load('en', disable=['parser', 'ner'])
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out


def visulaizer_of_LDA(content_list):
    stop_words = stopwords.words('english')

    data_words = list(sent_to_words(content_list))

    bigram = Phrases(data_words, min_count=5, threshold=100)
    trigram = Phrases(bigram[data_words], threshold=100)
    bigram_mod = Phraser(bigram)
    trigram_mod = Phraser(trigram)

    data_words_nostops = remove_stopwords(data_words, stop_words)
    data_words_bigrams = make_bigrams(data_words_nostops, bigram_mod)
    data_words_trigrams = make_trigrams(data_words_bigrams, bigram_mod, trigram_mod)
    data_lemmatized = lemmatization(data_words_trigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])

    id2word = corpora.Dictionary(data_lemmatized)
    texts = data_lemmatized
    corpus = [id2word.doc2bow(text) for text in texts]

    lda_model = LdaModel(corpus=corpus,
                         id2word=id2word,
                         num_topics=6,
                         random_state=100,
                         update_every=1,
                         chunksize=100,
                         passes=10,
                         alpha='auto',
                         per_word_topics=True)

    vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)

    return vis


def gather_data(file="data/US_Accidents_May19.csv"):
    with open(file, 'r+') as csv_file:
        data = pd.read_csv(csv_file, sep=',')
    return data.columns.values, data


if __name__ == '__main__':
    # Gather needed data and headers
    # headers, data = gather_data()
    # data.to_pickle('US_Accidents_May19.pickle')

    data = pd.read_pickle('data/US_Accidents_May19.pickle')

    description = data['Description'].tolist()
    description = [x for x in description if str(x) != 'nan']

    regex = {r'Accident|accident': ' ',
             r'\s+': ' '}

    reg_description = RegexReplacer.regex_multi_replacer(description, regex)

    LDA_vis = visulaizer_of_LDA(reg_description)

    with open('graph/LDA.pickle', 'wb') as file:
        pickle.dump(LDA_vis, file)

    LDA_vis = None
    with open('graph/LDA.pickle', 'rb') as file:
        LDA_vis = pickle.load(file)

    pyLDAvis.show(LDA_vis)

    # severity = data.loc[:, "Severity"]

    # y_co = TSNE().fit_transform(data, severity)

    # plt.scatter(y_co[0], y_co[1])
    # plt.show()



