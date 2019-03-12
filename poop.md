# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Robert Rhys Thomas

## Additional instructions

I have added -T and -P for specifying the test range and for using pos tags instead of words. -T is the percentage of the training set that you want to use. I have also automated the output of statistics, the program adds to the 'results' folder a folder with the name of the output file and will add to the folder the training/testing dataframes, the model and finally add to it a markdown file with the statistics, the program will also then zip up the training/test files so that they can easily be pushed/pulled to github. You need to remember to put the full file extension when specifying datafiles e.g results/50_lines/50_lines_training.csv. 

## Reporting for Part 4



## Reporting for Part Bonus 

I added a small bit of code that outputs the pos one-hot vectors instead of the words. 

<h2>Statistics for experiments</h1>
<p>The Following table shows the total statistics over all of the experiments.</p>

|    | file_name     |   lines | ngram   | pos   |   accuracy |   perplexity |
|----|---------------|---------|---------|-------|------------|--------------|
|  0 | 100_lines     |     100 | 2-gram  | False |   0.288073 |      55.4609 |
|  1 | 100_lines_n3  |     100 | 3-gram  | False |   0.246479 |      65.5333 |
|  2 | 100_lines_pos |     100 | 2-gram  | True  |   0.446927 |      69.1123 |
|  3 | 200_lines     |     200 | 2-gram  | False |   0.286672 |      97.3902 |
|  4 | 200_lines_pos |     200 | 2-gram  | True  |   0.409574 |     128.132  |