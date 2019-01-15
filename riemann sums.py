#Riemann Sum Calculator, Josiah Schmidt, Last Edited 1/14/2019
def f(x):
    return(x**2)    #returns the predefined function (x squared, in this case)

start=int(input("start point: "))   #input start of bounds
end=int(input("end point: "))       #input end of bounds
n=int(input("intervals: "))         #input number of intervals
if(n<1):                            #n cannot be 0 or negative
    raise ValueError('intervals cannot be zero or negative.') #throw an error
method=str(input("left, right, midpoint, trapezoidal, or simpsons rule: "))  #input method of riemann sum
width=(end-start)/n       #calculate with of intervals
Area=0                  #Area to be output later
if(method=="left"):
    for i in range(n):
        Area+=f(start+width*i)*width #left riemann sum
if(method=="right"):
    for i in range(n):
        Area+=f(end-width*i)*width #right riemann sum
if(method=="midpoint"):
    for i in range(n):
        Area+=f(start+(width/2)+width*i)*width  #midpoint riemann sum
if(method=="trapezoidal"):
    for i in range(n):
        avg=(f(start+width*i)+f(end-width*i))/2 #average between endpoints
        Area+=avg*width                       #trapezoidal riemann sum
if(method=="simpsons rule"):
    if(n%2==1):
        raise ValueError('Simpsons Rule requires an even number of intervals.') #throw an error
    midpt=0
    trap=0
    for i in range(n):                                  #finds trapezoidal sum
        avg=(f(start+width*i)+f(end-width*i))/2 
        trap+=avg*width
    for i in range(n):                                  #finds midpoint sum
        midpt+=f(start+(width/2)+width*i)*width
    Area=((2*midpt)+trap)/3                             #weighted average
        
print(Area) #output
