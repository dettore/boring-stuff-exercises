# The Collatz Sequence

def collatz(number):
    if (number%2) == 0:
        value=number//2
    else:
        value=3*number+1
        
    print(value)
    
    return(value)

try:
   inputVal=int(input('Enter an integer: '))
   retVal=inputVal
   while retVal !=1:
       retVal=collatz(retVal)
except ValueError:
    print('Not an integer value')




