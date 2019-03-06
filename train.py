import os, sys
import argparse
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# train.py -- Don't forget to put a reasonable amount code comments
# in so that we better understand what you're doing when we grade!

# add whatever additional imports you may need here.

def args():
    parser = argparse.ArgumentParser(description="Train a maximum entropy model.")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("datafile", type=str,
                        help="The file name containing the features.")
    parser.add_argument("modelfile", type=str,
                        help="The name of the file to which you write the trained model.")
    args = parser.parse_args()
    return args.datafile, args.ngram, args.modelfile

def read_datafile(datafile):
    print("reading data")
    data = pd.read_csv(datafile)
    vectors = []
    classes = []
    print("formatting")
    
    #print(data.values[:,-1])
    """
    for i in data.values:
        print('..')
        vector = list(i[:-1])
        classification = i[-1]
        vectors.append(vector)
        classes.append(classification)
    """

    
    vectors = np.array(vectors)
    classes = np.array(classes)
    print(vectors.shape)
    print(classes.shape)
    print("generating model")
    lr = LogisticRegression(multi_class='multinomial', solver='lbfgs', verbose=1)
    pre_pickled_data = lr.fit(data.values[:,:-1],data.values[:,-1], sample_weight=None)
    
    return pre_pickled_data
    

def pickling(data,modelfile):
    print("pickling")
    return pickle.dump(data, open(modelfile + '.p', "wb"))

if __name__ == "__main__":

    datafile, ngram, modelfile = args()
    data = read_datafile(datafile)
    exported_data = pickling(data, modelfile)
    print("Loading data from file {}.".format(datafile))
    print("Training {}-gram model.".format(ngram))
    print("Writing table to {}.".format(modelfile))




# YOU WILL HAVE TO FIGURE OUT SOME WAY TO INTERPRET THE FEATURES YOU CREATED.
# IT COULD INCLUDE CREATING AN EXTRA COMMAND-LINE ARGUMENT OR CLEVER COLUMN
# NAMES OR OTHER TRICKS. UP TO YOU.
