"""a=10
b=12
def add(a,b):
    return a+b

result=add(a,b)
print("The sum of a and b is:", result)"""

"""def calc(a,b,op):
    if op=='+':
        return a+b
    if op=='-':
        return a-b
    if op=='*':
        return a*b
    if op== '/':
        return a/b
    else:
        print("not corret operation")

a=int(input("enter number1:"))
b=int(input("enter number 2:"))
op=input("(enter operator (+,-,*,/)")
print(calc(a,b,op))"""

#printing n to 1 numbers repeatedly to understand recursion

"""def rev(n):
    
    if n!=0:
        print(n)
        rev(n-1)
    else:
        return 0
        

    
rev(10)"""

"""#printing sum of first n natural number to understand recursion

def rev(n,sum):
    
    if n!=0:
        sum=sum+n
        return rev(n-1,sum)
    else:
        return sum
        

    
print(rev(10,0))"""
"""
marks=[12,13,14,15,144,122]
print(marks[-3:-1])
 """