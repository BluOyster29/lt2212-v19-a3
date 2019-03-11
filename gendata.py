import os, sys, glob, argparse, numpy as np, pandas as pd

# gendata.py -- Don't forget to put a reasonable amount code comments
# in so that we better understand what you're doing when we grade!
# add whatever additional imports you may need here. You may not use the
# scikit-learn OneHotEncoder, or any related automatic one-hot encoders.

def args():
    '''This function creates and stores all the arg parsers, I put them in here because it felt a bit tidier.'''
    parser = argparse.ArgumentParser(description="Convert text to features")
    parser.add_argument("-N", "--ngram", metavar="N", dest="ngram", type=int, default=3, help="The length of ngram to be considered (default 3).")
    parser.add_argument("-S", "--start", metavar="S", dest="startline", type=int,
                    default=0,
                    help="What line of the input data file to start from. Default is 0, the first line.")
    parser.add_argument("-E", "--end", metavar="E", dest="endline",
                    type=int, default=None,
                    help="What line of the input data file to end on. Default is None, whatever the last line is.")
    parser.add_argument("-T", "--test", metavar="T", dest="test_range",
                    type=int, default=None,
                    help="How large will the test size be")
    parser.add_argument("-P",  dest="pos", action="store_true", default=False, help="Whether or not to use pos tags for model.")
    parser.add_argument("inputfile", type=str,
                    help="The file name containing the text data.")
    parser.add_argument("outputfile", type=str,
                    help="The name of the output file for the feature table.")
    args = parser.parse_args()
    return args.inputfile, args.outputfile, args.startline, args.endline, args.ngram, args.test_range, args.pos

def open_text(file_path , startline, endline, pos):
    '''function that goes through the text fiel and tokenizes. Function outpus 
    a matrix of every line and their tokens and the length of the vocabulary'''
    with open(file_path, "r", encoding="utf-8") as text:
        file = text.readlines()
        corpus =[] 
        line_tokenized = []
        lines = 0 #for counting how many lines in the text
        if pos == False:
            #loops return matrix containing words
            for line in file[startline:endline]:
                line_tokens = []
                tokenizing = line.split() #tokenises string by white space
                for i in tokenizing:
                    further_cleaning = i.split('/') #creates tuple of word and pos tag 
                    line_tokens.append(further_cleaning[0])
                    corpus.append(further_cleaning[0])
                line_tokenized.append(line_tokens)  
                lines += 1 
        else:
            #loops return matrix containing pos tags
            for line in file[startline:endline]:
                line_tokens = []
                tokenizing = line.split()
                for i in tokenizing:
                    further_cleaning = i.split('/')
                    line_tokens.append(further_cleaning[1])
                    corpus.append(further_cleaning[1])
                line_tokenized.append(line_tokens)  
                lines += 1 
    start_simbols = ['<start>', '<end>'] #adding start/end symbols to the corpus
    corpus += start_simbols
    vocab = sorted(list(set(corpus))) #list of tokens representing the vocabulary
    vocab_len= len(vocab)
    corpus_dic = {i:vocab.index(i) for i in vocab} #creates a dictionary of words and their place index in the vocabulary
    print('number of lines = ' + str(lines)) #recording number of lines
    return line_tokenized, corpus_dic, vocab_len 

def one_hot_encoder(corpus,vocabualary_size):
    '''Functin for one-hot encoding, the function creates a list the size of the vocabulary and 
    inserts a one at the index of the word in the vocabulary'''
    counter= 1
    one_hot_corpus = {}
    for token in corpus:
        one_hot = [0] * vocabualary_size
        one_hot[corpus[token]] = 1
        one_hot_corpus[token] = one_hot
        counter+=1
        #print('vocab item: ' + str(counter))    
    return one_hot_corpus #dictionary contains the one-hot vector of each token

def gen_ngrams(start_line, end_line, line_matrix, one_hot_matrix, n,test_size):
    '''Function goes through each line and turns the tokens into their one-hot representation, ultimately creating 
    a matrix of lines and their one-hot representations. I have also shuffled the lines so that the training and 
    test set can be taken from random samples within a range'''
    np.random.shuffle(line_matrix)
    training_size = len(line_matrix) - test_size #specifies how many lines belong to training
    training_lines,testing_lines = line_matrix[:training_size], line_matrix[training_size:] #slices the ranges
    training_set =[]
    for lines in training_lines:
        '''I couldn't think of a smarter way to add the start and end symbols so i'm afraid this is it.
        The program goes through the lines in the matrix converting the tokens, based on -N it will take the previous n
        grams'''
        lines.insert(0, '<start>')
        lines.insert(0, '<start>')
        lines.insert(0, '<start>')
        lines.insert(0, '<start>')
        lines.insert(-1, '<end>')
        lines.insert(-1, '<end>')
        lines.insert(-1,'<end>')
        lines.insert(-1, '<end>')
        n_one_hots = []
        for i in range(len(lines)):
            if n == 2:
                hotty = one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-1]]
                hotty.append(lines[i])
                n_one_hots.append(hotty)
            elif n == 3:
                hotty = one_hot_matrix[lines[i-3]] + one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-1]]
                hotty.append(lines[i])
                n_one_hots.append(hotty)
            elif n == 4:
                hotty = one_hot_matrix[lines[i-4]] + one_hot_matrix[lines[i-3]] + one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-1]]
                hotty.append(lines[i])
                n_one_hots.append(hotty)
        training_set += n_one_hots
    testing_set =[]
    #sepearte loop for testing set
    for lines in testing_lines:
        lines.insert(0, '<start>')
        lines.insert(0, '<start>')
        lines.insert(0, '<start>')
        lines.insert(0, '<start>')
        lines.insert(len(lines), '<end>')
        lines.insert(len(lines), '<end>')
        lines.insert(len(lines),'<end>')
        lines.insert(len(lines), '<end>')
        n_one_hots = []
        for i in range(len(lines)):
            if n == 2:
                hotty = one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-1]]
                hotty.append(lines[i])
                n_one_hots.append(hotty)
            elif n == 3:
                hotty = one_hot_matrix[lines[i-3]] + one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-1]]
                hotty.append(lines[i])
                n_one_hots.append(hotty)
            elif n == 4:
                hotty = one_hot_matrix[lines[i-4]] + one_hot_matrix[lines[i-3]] + one_hot_matrix[lines[i-2]] + one_hot_matrix[lines[i-1]]
                hotty.append(lines[i])
                n_one_hots.append(hotty)
        testing_set += n_one_hots
    return training_set, testing_set
    
def output_file(training_set, testing_set, output): 
    '''Function generates pd dataframe so that one can view the data. Two files are then outputted
    a training and test csv file.''' 
    print('generating dataframe')  
    training = pd.DataFrame(training_set)
    testing = pd.DataFrame(testing_set)
    print('outputting')
    training.to_csv(path_or_buf=output + '_training.csv', index=False)
    testing.to_csv(path_or_buf=output + '_testing.csv', index=False)

def main():
    '''I have put the main commands into this function just to tidy it up a bit. Please let me know if this is not proper practice, 
    it is more for my ocd because it's nice to see all the functions collapsed'''
    input, output, startline, endline, ngrams, test_size,pos = args()
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
    line_matrix, vocab, v = open_text(input, startline, endline, pos)
    print(len(vocab))
    print('generating one-hots\n')
    one_hot_matrix = one_hot_encoder(vocab,v)
    print('generating one-hot matrix\n')
    training_set,testing_set  = gen_ngrams(startline, endline, line_matrix,one_hot_matrix,ngrams, test_size)
    print('outputting file\n')
    output_file(training_set, testing_set, output)
    print(output)

if __name__ == '__main__':
    main()

# THERE ARE SOME CORNER CASES YOU HAVE TO DEAL WITH GIVEN THE INPUT
# PARAMETERS BY ANALYZING THE POSSIBLE ERROR CONDITIONS.
