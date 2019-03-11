import numpy
from scipy.stats import entropy
from math import log2
'''

def create_random(total_matrix,test_range):
    x = numpy.array(total_matrix)
    numpy.random.shuffle(x)
    training,test = x[:3,:], x[3:,:]
    print(training)
    print(test)

'''

if __name__ == "__main__":
    '''
    test_range = 2
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
    print(create_random(matrix,test_range))
    '''
    probs = [[4,4,2,3,5,1]]

    nobs = {'cat':3,'dog':2,'pig':5}

    bobs = [3,2,5]

    print(-sum([i * log2(i) for i in bobs]))
    
    print(entropy(pk=bobs,base=2))

    #print(dik)
    