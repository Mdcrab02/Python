import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    # Your code here 
    global CURRENTRABBITPOP 
    global MAXRABBITPOP  
    for n in xrange(CURRENTRABBITPOP):
        #for each rabbit in the population
        p_rabit_reproduction = 1.0 - (CURRENTRABBITPOP / float(MAXRABBITPOP))
        #this is the chance of a new rabbit being born, becomes less at high pop. 
        if random.random() <= p_rabit_reproduction and CURRENTRABBITPOP < MAXRABBITPOP:
            #if a random number is within the probability and there are fewer than 1000
            #rabits 
            CURRENTRABBITPOP += 1
            #a new rabbit is born

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    # Your code here 
    global MAXRABBITPOP 
    global CURRENTFOXPOP 

    for i in xrange(CURRENTFOXPOP): 
        p_fox_eats_rabbit = CURRENTRABBITPOP / float(MAXRABBITPOP) 
        if random.random() <= p_fox_eats_rabbit and CURRENTRABBITPOP > 10:
            #if there are more than 10 rabbits and the fox gets one
            CURRENTRABBITPOP -= 1 #that's one rabbit gone 
            if random.random() <= 1/3.0: #there is a 1/3 chance of a new fox
                CURRENTFOXPOP += 1 #the fox is born
        else: #if the fox doesn't get a rabbit 
            if random.random() <= 9/10.0 and CURRENTFOXPOP > 10:
                #if there are more than 10 foxes, there is a chance the fox dies 
                CURRENTFOXPOP -=1 #one less fox
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    # Your code here 
    rabbit_populations = [] 
    fox_populations = [] 
    for i in xrange(numSteps):
        #for each step number, call the following methods 
        rabbitGrowth() 
        foxGrowth() 
        rabbit_populations.append(CURRENTRABBITPOP) 
        fox_populations.append(CURRENTFOXPOP) 
        #append the lists -/+ a rabbit/fox
    return (rabbit_populations, fox_populations) 
(r, f) = runSimulation(200) 
pylab.figure(1) 
pylab.plot(r, 'b.') 
pylab.plot(f, 'r.') 
x_vals = pylab.array(range(len(r))) 
a, b, c = pylab.polyfit(x_vals, r, 2) 
est_yvals = a*x_vals**2 + b*x_vals + c 
pylab.plot(est_yvals, 'b-') 
pylab.show() 
