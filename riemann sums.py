#Riemann Sum Calculator, Josiah Schmidt, Last Edited 1/16/2019
#If you downloaded this program off GitHub, please read the readme for instructions.
import math     #import more advanced math functions
def f(x):                   
    return(math.sin(x**2))    #returns the predefined function (sine of x squared, in this case)

def rsum():
    start=int(input("start point: "))   #input start of bounds
    end=int(input("end point: "))       #input end of bounds
    n=int(input("intervals: "))         #input number of intervals
    if(n<1):                            #n cannot be 0 or negative
        raise ValueError('intervals cannot be zero or negative.') #throw an error
    method=str(input("left, right, midpoint, trapezoidal, or simpsons rule: "))  #input method of riemann sum
    width=(end-start)/n       #calculate with of intervals
    Area=0                  #Area to be output later
    if(method=="left"):         #if specified left endpoint method
        for i in range(n):      #loop for number of intervals
            Area+=f(start+width*i)*width #left riemann sum
    if(method=="right"):        #if specified right endpoint method
        for i in range(n):      #loop for number of intervals
            Area+=f(end-width*i)*width #right riemann sum
    if(method=="midpoint"):     #if specified midpoint method
        for i in range(n):      #loop for number of intervals
            Area+=f(start+(width/2)+width*i)*width  #midpoint riemann sum
    if(method=="trapezoidal"):          #if selected method trpaezoidal
        for i in range(n):          #loop for number of intervals
            avg=(f(start+width*i)+f(end-width*i))/2 #average between endpoints
            Area+=avg*width                       #trapezoidal riemann sum
    if(method=="simpsons rule"):    #if specifies simpsons rule
        if(n%2==1):                 #simpsons rule requires even number of intervals
            raise ValueError('Simpsons Rule requires an even number of intervals.') #throw an error
        midpt=0     
        trap=0
        for i in range(n):      #loops for number of intervals                            
            avg=(f(start+width*i)+f(end-width*i))/2     #uses trapezoidal sum algorithm
            trap+=avg*width         #finds trapezoidal sum
        for i in range(n):           #loops for number of intervals                
            midpt+=f(start+(width/2)+width*i)*width   #finds midpoint sum
        Area=((2*midpt)+trap)/3                             #weighted average
            
    return(Area) #output

print(rsum())   #run riemann sum
