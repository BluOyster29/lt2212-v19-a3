# LT2212 V19 Assignment 3

From Asad Sayeed's statistical NLP course at the University of Gothenburg.

My name: Robert Rhys Thomas

## Additional instructions

I have added -T and -P for specifying the test range and for using pos tags instead of words. 

## Reporting for Part 4

I testing the program over 100 lines over various parts of the data. A big proble I came into was the issue that the logistic regression classifier was taking far too long to create the model. Anything over 100 lines and It would take an unreasonable amount of time to execute therefore I limit the chunks to around 100 lines. I also limited the classifiers epochs to 20. I did this to save processing power, this does however throw a ConvergenceWarning as coef has not converged, I think for this experiment we can allow this. 

## Reporting for Part Bonus 

I added a small bit of code that outputs the pos one-hot vectors instead of the words. I found when modeling over part os speech tags the accuracy was much higher but the perplexity was also higher suggesting either a bug in the calculations 
