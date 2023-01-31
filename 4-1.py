# Design a Python function to find the Max of three numbers.
def maxi(a,b,c):
    if a<b:
        if b<c:    
            return c
        return b
    return a
a,b,c=map(int,input("Enter the numbers : ").split())
print("Maximum number is : ",maxi(a,b,c))

# Enter the numbers : 77 98 7798
# Maximum number is :  7798