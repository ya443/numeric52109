###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

import simple_package as sp

if __name__ == '__main__':
    ## Define two numbers
    a = 1
    b = 2
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The sum of {a} and {b} is {sp.add(a,b)}")
    
    
    # *Comments:*
    # I correctly imported the operations module from the simple_package package and changed
    # the statment to correctly name the add function.    
    # The output of the two print statements should be identical.