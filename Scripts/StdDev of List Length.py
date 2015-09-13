def meanOfElements(L):
    sumOfElements = 0
    count = 0
    for i in L:
        sumOfElements += i
        count += 1
    return float(float(sumOfElements)/float(count))
    
def squareX(x):
    return x**2
    
def varianceElem(i,L):
    return squareX(i-meanOfElements(L))
    
def sigmaVar(L):
    sumHolder = 0.0
    for i in L:
        sumHolder += varianceElem(i,L)
    return sumHolder
        
def sqrt(x):
    return x**(0.5)
    
def strLenList(L):
    '''takes in a list of strings and returns a list of
        the length for each string'''
    lenList = []
    for i in L:
       lenList.append(len(i)) 
    return lenList

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('Nan')
    else:
        firstThing = 0.0
        #firstThing += sigmaVar(L)  #use this if not a list of strings
        firstThing += sigmaVar(strLenList(L))
        count = 0
        for i in L:
            count +=1
        return sqrt(firstThing/count)
    
    
print stdDevOfLengths(['apples','oranges','kiwis','pineapples'])
#print stdDevOfLengths([])