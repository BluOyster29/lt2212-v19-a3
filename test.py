import os, sys, argparse,pickle,numpy as np, pandas as pd, subprocess
from sklearn.linear_model import LogisticRegression
from scipy.stats import entropy
from math import log2

# test.py -- Don't forget to put a reasonable amount code comments
# in so that we better understand what you're doing when we grade!
# add whatever additional imports you may need here.

def args():

    '''again i have put the args inside this function to keep them tidy'''

    parser = argparse.ArgumentParser(description="Test a maximum entropy model.")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("datafile", type=str,
                        help="The file name containing the features in the test data.")
    parser.add_argument("modelfile", type=str,
                        help="The name of the saved model file.")
    args = parser.parse_args()

    return args.ngram,args.datafile, args.modelfile

def open_pickle_jar(modelfile):

    """small function for opening the pickly file and returning the model"""

    pickleFile = open(modelfile, 'rb')
    regression_model = pickle.load(pickleFile)
    pickleFile.close()

    return regression_model

def process_test_file(datafile):

    """short function for reading the csv file, converting the data into a matrix 
    and sperating the vectors from the classes"""
    data = pd.read_csv(datafile).values

    vectors = []
    classes = []

    for i in data:
        vector = list(i[:-1])
        classification = i[-1] #classes are the last column of the index
        vectors.append(vector)
        classes.append(classification)

    return np.array(vectors), classes

def test_model(model,vectors,classes):

    """logisitic regression model is applied to find statistics based on the training data. 
    firstly i use the built in functions to generate a matrix of probabilities, log_probs and the accuracy score.
    I then use the probabilities to calculate the perplexity"""

    predictions = model.predict(vectors) #built-in matrix of predictions
    accuracy = model.score(vectors, classes, sample_weight=None) #built-in accuracy score based on actual classes
    probs = model.predict_proba(vectors) #matrix of probabilites for each class
    log_probs = model.predict_log_proba(vectors) #log probs of the above
    pred_probs = []

    for i in range(len(vectors)):

        """This loop goes through each vector in the matrix, finds the max probability (which will be the chosen class)
        and appends it to a list of max(probs)"""

        vector = vectors[i]
        probs=model.predict_proba([vector])[0]
        pred_probs.append(max(probs))

    perplexity = 2**(entropy(pred_probs)) #this is calculated using built-in entropy function
    
    return accuracy, perplexity

def main():

    """again everything is neatly packed up in a main function"""

    ngram,datafile, modelfile = args()
    training_file = datafile[:-11] +'training.csv'
    zip_file = '/'.join(datafile.split("/")[:2]) + '/'
    model = open_pickle_jar(modelfile)
    vectors,classes = process_test_file(datafile)
    accuracy, perplexity = test_model(model, vectors,classes)
    print("Loading data from file {}.".format(datafile))
    print("Loading model from file {}.".format(modelfile))
    print("Testing {}-gram model.".format(ngram))
    print("Accuracy is {}".format(accuracy))
    print("Perplexity is {}".format(perplexity))
    f = open(modelfile[:-2] +'.md', 'w+')
    f.write("<h1>Statistics<h1>\n")
    f.write("<h2>Datafile:</h2>\n<p>Loading data from file {}.</p>\n".format(datafile))
    f.write("<h2>Loading model from file {}.</h2>\n\n".format(modelfile))
    f.write("<h2>Testing {}-gram model.\n\n".format(ngram))
    f.write("<h2>Accuracy: {}.</h2>\n\n".format(accuracy))
    f.write("<h2>Perplexity: {}.</h2>\n\n".format(perplexity))
    f.close()
    one = subprocess.call(
    'zip ' + zip_file + 'dataframes ' + datafile + ' ' +  training_file,
    shell=True
    )
    one = subprocess.call(
    'rm ' + datafile + ' ' + training_file,
    shell=True
    )
    
if __name__ == "__main__":
    main()
    
