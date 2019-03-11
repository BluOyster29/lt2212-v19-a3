import os, sys, argparse, numpy as np, pandas as pd, pickle
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# train.py -- Don't forget to put a reasonable amount code comments
# in so that we better understand what you're doing when we grade!
# add whatever additional imports you may need here.

def args():

    """again more args here than on a pirate ship"""

    parser = argparse.ArgumentParser(description="Train a maximum entropy model.")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("datafile", type=str,
                        help="The file name containing the features.")
    parser.add_argument("modelfile", type=str,
                        help="The name of the file to which you write the trained model.")
    args = parser.parse_args()
    
    return args.datafile, args.ngram, args.modelfile

def read_datafile(datafile, modelfile):

    """function that reads the data file then formats the data into vectors and classes
    to be passed to the logistic regression function, I have used the 'saga' solver as I believed
    this might be quicker (due to a stranger on the internet), I have also set max_ter to 20 as the 
    function seems to take an awfully long time on anything over 100 lines"""

    print("reading data")
    bata = pd.read_csv(datafile)
    print("generating model")
    lr = LogisticRegression(multi_class='multinomial', solver='lbfgs', n_jobs=-1, max_iter=20, verbose=1)
    print("fitting")
    pre_pickled_data = lr.fit(X=bata.iloc[:,:-1],y=bata.iloc[:,-1], sample_weight=None).sparsify()
    print("pickling")
    ogorki = pickle.dump(pre_pickled_data, open(modelfile + '.p', "wb")) #outputting pickled file

    return ogorki #ogorki is polish for pickled cucumber, my favourite snack
    
def main():

    #main function
    datafile, ngram, modelfile = args()
    data = read_datafile(datafile,modelfile)
    print("Loading data from file {}.".format(datafile))
    print("Training {}-gram model.".format(ngram))
    print("Writing table to {}.".format(modelfile))

if __name__ == "__main__":
    main()
    
# YOU WILL HAVE TO FIGURE OUT SOME WAY TO INTERPRET THE FEATURES YOU CREATED.
# IT COULD INCLUDE CREATING AN EXTRA COMMAND-LINE ARGUMENT OR CLEVER COLUMN
# NAMES OR OTHER TRICKS. UP TO YOU.
