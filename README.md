# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Robert Rhys Thomas

## Additional instructions

I have added -T and -P for specifying the test range and for using pos tags instead of words. -T is the percentage of the training set that you want to use. I have also automated the output of statistics, the program adds to the 'results' folder a folder with the name of the output file and will add to the folder the training/testing dataframes, the model and finally add to it a markdown file with the statistics, the program will also then zip up the training/test files so that they can easily be pushed/pulled to github. You need to remember to put the full file extension when specifying datafiles e.g results/50_lines/50_lines_training.csv. I have also added a few extra scripts so that the statistics printing is automated, the program 'export_stats.py' will, after the experiments have been completed, collate all of the stats and output them to a markdown table and append them to README.md. 

## Reporting for Part 4

The table below shows the results, I'll give a quick key to explain the headings.
* file_name: This is the name of the outputted file
* lines: This is the number of lines chosen, it is essentially the start line minus the end line. The training/testing ration is set in gendata.py but is typically 80/20
* ngram: This is the output to the -N argument and specifices n's value
* accuracy: This is the model's 'scores' as provided by the built-in function 'model.score()'
* perplexity: This is calculated by myself therefore may not be perfect but the output does seem to fit my hypotheses

My initial hypothesis consisted of expectations that the larger the training data the greater accuracy as we have more data to learn from. I believe that as the training range gets larger that can give more oppertunity for uncertainty as the probabilities will get smaller therefore I predicted that the perplexity will get larger. This does somewhat seem to be the case if we look at the results. 


Instead explain any hypotheses you made, how you tested them, and what you observed.  This need not be more than 2-4 paragraphs worth of text and will be graded on reasonable effort.

## Reporting for Part Bonus 

I have added the argument -P this will allow the user to choose between the words or the part of speech. This has given some interesting results when comparing to the same experiment but with just the word

<h2>Statistics for experiments</h2>
<p>The Following table shows the total statistics over all of the experiments.</p>

|    | file_name        |   lines | ngram   | pos   |   accuracy |   perplexity |
|----|------------------|---------|---------|-------|------------|--------------|
|  0 | 100_lines        |     100 | 2-gram  | False |   0.288073 |      55.4609 |
|  1 | 100_lines_n3     |     100 | 3-gram  | False |   0.246479 |      65.5333 |
|  2 | 100_lines_n4     |     100 | 4-gram  | False |   0.283993 |      52.5624 |
|  3 | 100_lines_pos    |     100 | 2-gram  | True  |   0.446927 |      69.1123 |
|  4 | 100_lines_pos_n4 |     100 | 4-gram  | True  |   0.400314 |      74.7126 |
|  5 | 200_lines        |     200 | 2-gram  | False |   0.286672 |      97.3902 |
|  6 | 200_lines_pos    |     200 | 2-gram  | True  |   0.409574 |     128.132  |
|  7 | 500_lines_n2     |     500 | 2-gram  | False |   0.278261 |     199.712  |
|  8 | 500_lines_pos_n2 |     500 | 2-gram  | True  |   0.514554 |     179.641  |