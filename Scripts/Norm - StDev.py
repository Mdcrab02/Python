def Mean(l):
    n = 0
    total = 0.0
    for i in l:
        total = total + i
        n = n+1
    return total/n

#print Mean([1,2,3,4,5,6])
def Sqrt(x):
    return x**(0.5)

#print Sqrt(36)    
def Sum(l):
    total = 0.0
    for i in l:
        total = total + i
    return total

#print Sum([1,2,3,4])

def SumDiff(l):
    total = 0.0
    for i in l:
        total = total + ((i - Mean(l))**2)
    return total
    
def CountLen(l):
    n = 0
    for i in l:
        n = n + 1
    return n
    
print CountLen([1,2,3,4])      
