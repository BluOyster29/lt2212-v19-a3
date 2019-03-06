import os, sys
import glob
import argparse
import numpy as np
import pandas as pd

# gendata.py -- Don't forget to put a reasonable amount code comments
# in so that we better understand what you're doing when we grade!

# add whatever additional imports you may need here. You may not use the
# scikit-learn OneHotEncoder, or any related automatic one-hot encoders.

def args():
    parser = argparse.ArgumentParser(description="Convert text to features")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int,
                    default=0,
                    help="What line of the input data file to start from. Default is 0, the first line.")
    parser.add_argument("-E", "--end", metavar="E", dest="endline",
                    type=int, default=None,
                    help="What line of the input data file to end on. Default is None, whatever the last line is.")
    parser.add_argument("inputfile", type=str,
                    help="The file name containing the text data.")
    parser.add_argument("outputfile", type=str,
                    help="The name of the output file for the feature table.")
    args = parser.parse_args()
    '''
    print("Loading data from file {}.".format(args.inputfile))
    
    print("Starting from line {}.".format(args.startline))
    if args.endline:
        print("Ending at line {}.".format(args.endline))
        
    else:
        print("Ending at last line of file.")
    print("Constructing {}-gram model.".format(args.ngram))
    print("Writing table to {}.".format(args.outputfile))   
    '''
    return args.inputfile, args.outputfile, args.startline, args.endline, args.ngram

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
        #print('vocab item: ' + str(counter))    
    return one_hot_corpus

def gen_ngrams(start_line, end_line, line_matrix, one_hot_matrix, n):
    output_file = line_matrix[start_line -1:end_line -1]
    line_hots = []
    #model = {}
    for lines in output_file:
        n_one_hots = []
        for i in range(4,len(lines)):
            if n == 2:
                hotty = one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-1]]
                #hotty.append(lines[i] + '|' + lines[i-1])
                #model[lines[i] + '|' + lines[i-1]] = one_hot_matrix[lines[i]] + one_hot_matrix[lines[i-1]]
                hotty.append(lines[i])
                n_one_hots.append(hotty)
                #model[lines[i]] = one_hot_matrix[lines[i]] + one_hot_matrix[lines[i-1]]
                #n_one_hots.append((hotty,lines[i]))
                #n_one_hots.append(lines[i])
            elif n == 3:
                hotty = one_hot_matrix[lines[i-3]] + one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-1]]
                #hotty.append(lines[i] + '|' + lines[i-1] + '|' + lines[i-2])
                #model[lines[i] + '|' + lines[i-1] + '|' + lines[i-2]] = one_hot_matrix[lines[i]] + one_hot_matrix[lines[i-1]] + one_hot_matrix[lines[i-2]]
                hotty.append(lines[i])
                n_one_hots.append(hotty)
                #model[lines[i]] = one_hot_matrix[lines[i]] + one_hot_matrix[lines[i-1]] + one_hot_matrix[lines[i-2]]
                #n_one_hots.append((hotty, lines[i]))
                #n_one_hots.append(lines[i])
            elif n == 4:
                hotty = one_hot_matrix[lines[i-4]] + one_hot_matrix[lines[i-3]] + one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-1]]
                #hotty.append(lines[i] + lines[i-1] + '|' + lines[i-2] + '|' + lines[i-3])
                #model[lines[i] + lines[i-1] + '|' + lines[i-2] + '|' + lines[i-3]] = one_hot_matrix[lines[i]] + one_hot_matrix[lines[i-1]] + one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-3]]
                hotty.append(lines[i])
                n_one_hots.append(hotty)
                #model[lines[i]] = one_hot_matrix[lines[i]] + one_hot_matrix[lines[i-1]] + one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-3]]
                #n_one_hots.append((hotty, lines[1]))
                #n_one_hots.append(lines[i])
        line_hots += n_one_hots
    #print(line_hots)
    return np.array(line_hots)
    
def output_file(training_lines, output):  
    print('generating dataframe')  
    df = pd.DataFrame(training_lines)
    print('outputting')
    df.to_csv(path_or_buf=output + '.csv', index=False)
    
if __name__ == '__main__':
    input, output, startline, endline, ngrams = args()
    line_break = "-" * 30 + "\n"
    print(line_break)
    print("File Stats")
    print(line_break)
    print("Input File is {}".format(input))
    print("output File is {}".format(output))
    print("Startline is {}".format(startline))
    print("Endline is {}".format(endline))
    print("Number of ngrams is {}".format(ngrams))
    print(line_break)
    print('formatting lines, generating vocab\n')
    line_matrix, vocab, v = open_text(input)
    print('generating one-hots\n')
    one_hot_matrix = one_hot_encoder(vocab,v)
    print('generating one-hot matrix\n')
    training_lines = gen_ngrams(startline, endline, line_matrix,one_hot_matrix,ngrams)
    print('outputting file\n')
    output_file(training_lines, output)
    #print(output)
    

'''
import gendata as t
input, output, startline, endline, ngrams = "brown_data/brown_rga.txt", "poop.txt", 1, 2, 2
line_matrix, vocab, v = t.open_text(input)
one_hot_matrix = t.one_hot_encoder(vocab,v)
training_lines = t.training_lines(startline, endline, line_matrix)
print(t.gen_ngrams(training_lines))
'''

# THERE ARE SOME CORNER CASES YOU HAVE TO DEAL WITH GIVEN THE INPUT
# PARAMETERS BY ANALYZING THE POSSIBLE ERROR CONDITIONS.
