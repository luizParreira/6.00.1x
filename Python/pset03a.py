
# Helper function
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)




def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    i = start
    r = 0
    while i < stop:
        r += f(i) * step
        i += step
    return r



print "Test Case 1: " + str(radiationExposure(0, 5, 1))
print ''
print "Test Case 2: " + str(radiationExposure(5, 11, 1))
print ''
print "Test Case 3: " + str(radiationExposure(0, 11, 1))
print ''
print "Test Case 4: " + str(radiationExposure(40, 100, 1.5))