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

My initial hypothesis consisted of expectations that the larger the training data the greater accuracy as we have more data to learn from. I believe that as the training range gets larger that can give more oppertunity for uncertainty as the probabilities will get smaller therefore I predicted that the perplexity will get larger. This does somewhat seem to be the case if we look at the results. I tested the set by taking a range of lines, shuffling the lines then randomly choosing the test and training data. All of the experiments used the training/testing ratio pf 80/20. I have also experimented by changing the amount of n and choosing whether or not to inclue pos tags. 

The first experiment performed was on 100 lines. The perplexity is low, signifying an efficient model and the accuracy is relatively good, just under 0.3. When extending n to 3 the perplexity drops and the accuracy rises, this is suggesting that n=3 makes a good model. The 200 line experiment gave a similar accuracy of just under 0.3 however the perplexity has risen by nearly double. This is an interesting outcome as it is suggesting that a larger model is less efficient. If we add one to n the accuracy rises to 0.5 which is good but as the accuracy rises so does the perplexity but the perplexity is not much larger than n=2. At the other end of the scale, on the lines of 1000 the accuracy has not improved but the perplexity has risen by around 600%, this is showing that this model is not the most efficient. 

The highest accuracy was achieved with n=3 for 200 lines, The accuracy os 0.51 and the perplexity os 109. Though this is quite a high perplexity, the accuracy is relatively good, this suggests that for the model it is good to have a lower training range but have a wide feature vector.

## Reporting for Part Bonus 

The POS feature has given some interesting results. The accuracy is much higher but the perplexity is not that different. Compared to with POS not applied the pos models are about 0.2 more accurate than the word_vector model. This possibly due to the fact that the length of the vectors is a lot shorter for pos due to the vocabulary being much shorter. The model also takes much less time to train

<h2>Statistics for experiments</h2>
<p>The Following table shows the total statistics over all of the experiments.</p>

|    | file_name         |   lines | ngram   | pos   |   accuracy |   perplexity |
|----|-------------------|---------|---------|-------|------------|--------------|
|  0 | 1000_lines_n2     |    1000 | 2-gram  | False |   0.287221 |     336.599  |
|  1 | 1000_lines_pos_n2 |    1000 | 2-gram  | True  |   0.439509 |     356.859  |
|  2 | 100_lines         |     100 | 2-gram  | False |   0.288073 |      55.4609 |
|  3 | 100_lines_n3      |     100 | 3-gram  | False |   0.317073 |      51.0392 |
|  4 | 100_lines_n4      |     100 | 4-gram  | False |   0.283993 |      52.5624 |
|  5 | 100_lines_pos     |     100 | 2-gram  | True  |   0.446927 |      69.1123 |
|  6 | 100_lines_pos_n3  |     100 | 3-gram  | True  |   0.385124 |      74.1671 |
|  7 | 100_lines_pos_n4  |     100 | 4-gram  | True  |   0.400314 |      74.7126 |
|  8 | 200_lines         |     200 | 2-gram  | False |   0.286672 |      97.3902 |
|  9 | 200_lines_n3      |     200 | 3-gram  | False |   0.51857  |     109.526  |
| 10 | 200_lines_pos     |     200 | 2-gram  | True  |   0.409574 |     128.132  |
| 11 | 200_lines_pos_n3  |     200 | 3-gram  | True  |   0.335646 |      97.5306 |
| 12 | 500_lines_n2      |     500 | 2-gram  | False |   0.278261 |     199.712  |
| 13 | 500_lines_pos_n2  |     500 | 2-gram  | True  |   0.514554 |     179.641  |
