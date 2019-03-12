import subprocess,os,pandas as pd, numpy as np
import matplotlib.pyplot as plt
import tabulate as t

def generate_stats():
    statistics = []
    for subdir, dirs, files in os.walk('results'):
        for x in files:
            if '.md' in str(os.path.join(subdir, x)):
                statistics.append(subdir + '/' + x)
             
    stat_model = []
    columns = ['file_name','lines', 'ngram','pos','accuracy','perplexity']
    
    for stat in sorted(statistics):
        with open(stat, 'r') as data:
            lines = data.readlines()
            total_lines = lines[1].split(' ')[4].split('/')[1].split('_')[0]
            train_test = lines[1].split(' ')[4].split('/')[1]
            accuracy = float(lines[7].split(' ')[1][:-6])
            perplexity = float(lines[9].split(' ')[1][:-6])
            if 'pos' in train_test:
                pos = True
            else:
                pos = False
            ngram =  lines[5].split(' ')[1]
            stat_model.append([train_test,total_lines,ngram,pos,accuracy,perplexity])

    df = pd.DataFrame(stat_model, columns=columns)
    return df

if __name__ == "__main__":

    df = generate_stats()
    x = open('README.md','r')
    text = ''.join(x.readlines())
    f = open('poop.md', 'w+')
    f.write(text)
    f.write('\n')
    x.close()
    f.write('<h2>Statistics for experiments</h1>\n')
    f.write(t.tabulate(df,tablefmt="github", headers="keys"))
    f.close()
    




