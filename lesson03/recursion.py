# Recursion...calling a function within itself

def sayhi():
    #print("Hi Michael")
    sayhi()


# Write a function that accepts a number and returns the factorials of that number
# factorial of 5 is 5*4*3*2*1
# in general n * (n - 1) * (n - 2) * ... * 1
# n * (n - 1)!

# Solving the problem using traditional method
def factorial_traditional(num: int) -> int:
    result = 1
    while num > 1:
        result *= num # result = result * num
        num -= 1 # num = num - 1
       
    
    return result

def factorial_recursion(num: int) -> int:
    if num < 2:
        return 1
    else:
        return num * factorial_recursion(num - 1)

#print(factorial_recursion(6))

print(factorial_traditional(5))
