#Exceptions
#print(10/0)

print("This is working")

#Age for over 18
age = int(input("Enter your age: "))

if age <18:
    raise Exception("You are {} years. Which is below the age limit of 18 years".format(age))
#AssertionError
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."


# handles zerodivision exception    
try:
    k = 5/0 # raises divide by zero exception.
    print(k)
    
# handles zerodivision exception    
except ZeroDivisionError:   
    print("Can't divide by zero")
        
finally:
    # this block is always executed 
    # regardless of exception generation.
    print('This is always executed') :   
    print("Can't divide by zero")


