
import argparse, operator, os, numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
from nltk import word_tokenize, FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


parser = argparse.ArgumentParser(description='Reads a text and give us analysis')
parser.add_argument("filename", help="takes folder name name as argument", type=str)
parser.add_argument("-B", help="shows top words and counts", type=int)
parser.add_argument("--to-lower", help="processes the text as lower case", action = "store_true")
parser.add_argument("-T", help="counts will be transformed from raw counts into tf-idf", action ="store_true")
parser.add_argument("-S", help="sklearn will transform document vector to dimensionality n", type=int)

def open_text(file_path):
    '''function that goes through the text fiel and tokenizes. Function outpus 
    a matrix of every line and their tokens and the length of the vocabulary'''

    with open(file_path, "r", encoding="utf-8") as text:
        corpus =[]
        line_tokenized = []
        lines = 0
        for line in text:
            
            line_tokens = []
            tokenizing = line.split()
            for i in tokenizing:
                further_cleaning = i.split('/')
                line_tokens.append(further_cleaning[0])
                corpus.append(further_cleaning[0])

            line_tokenized.append(line_tokens)  
            lines += 1 
    vocab = sorted(list(set(corpus)))
    vocab_len= len(vocab)
    corpus_dic = {i:vocab.index(i) for i in vocab}
    print('number of lines = ' + str(lines))
    return line_tokenized, corpus_dic, vocab_len 

def one_hot_encoder(corpus,vocabualary_size):
    counter= 1
    one_hot_corpus = {}
    for token in corpus:
        one_hot = [0] * vocabualary_size
        one_hot[corpus[token]] = 1
        one_hot_corpus[token] = one_hot
        counter+=1
        print('vocab item: ' + str(counter))    
    return one_hot_corpus

if __name__ == "__main__":
    
    line_matrix, vocab, v = open_text('brown_data/brown_rga.txt')
    one_hot_matrix = one_hot_encoder(,vocab,v)
    
'''
import testing as t
line_matrix, vocab, v = t.open_text('brown_data/brown_rga.txt')
corpus = one_hot_matrix = t.one_hot_encoder(line_matrix,vocab,v)

'''