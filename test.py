import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

# test.py -- Don't forget to put a reasonable amount code comments
# in so that we better understand what you're doing when we grade!

# add whatever additional imports you may need here.

def args():
    parser = argparse.ArgumentParser(description="Test a maximum entropy model.")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("datafile", type=str,
                        help="The file name containing the features in the test data.")
    parser.add_argument("modelfile", type=str,
                        help="The name of the saved model file.")
    args = parser.parse_args()
    return args.ngram, args.datafile, args.modelfile

def open_pickle_jar(modelfile):
    pickleFile = open(modelfile, 'rb')
    regression_model = pickle.load(pickleFile)
    pickleFile.close()
    return regression_model

def process_test_file(datafile):
    data = pd.read_csv(datafile).values
    vectors = []
    classes = []
    for i in data:
        vector = list(i[:-1])
        classification = i[-1]
        vectors.append(vector)
        classes.append(classification)
    
    return data

def test_model(model,test_file):
    vectors = []
    classes = []

    for i in test_file:
        vector = list(i[:-1])
        classification = i[-1]
        vectors.append(vector)
        classes.append(classification)

    
    predictions = model.predict(vectors)
    '''
    for i in range(len(predictions)):
        if predictions[i] == classes[i]:
            print('True')
        else:
            print("False")
    '''
    #print(model.predict_log_proba(vectors))

    print(model.score(vectors, classes, sample_weight=None))
    print(model.predict(vectors))
    print(model.predict_log_proba(vectors))


if __name__ == "__main__":

    ngram, datafile, modelfile = args()
    model = open_pickle_jar(modelfile)
    test_file = process_test_file(datafile)
    testing_model = test_model(model, test_file)

    '''
    print("Loading data from file {}.".format(datafile))
    print("Loading model from file {}.".format(modelfile))
    print("Testing {}-gram model.".format(ngram))
    print("Accuracy is ...")
    print("Perplexity is...")
    '''
