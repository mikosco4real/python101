# count = 0

# while count< 10:
#     print("I just mastered the while loop")
#     count = count + 1


n = 10
sum = 0
i = 1

while sum < n:
    sum = sum + i
    print(sum)

counter = 0

# while counter < 3:
#     print ("inside loop")
#     counter += 1
# else: 
#     print("broken free") 

# text = "python"

# for i in text:
#     print (i)

# for count in range(1,21):
#     print (count)

# number = int(input("Enter number: "))

# for count in range(1,13):
#     product = number * count
#     print(f"{number} x {count} = {product}")
#     count+=1

# genre = ['pop','rock','jazz']

# for i in range(len(genre)):
#     print(genre[i])
    
# def fibonacci(num: int) -> int:
#     if num >= 0 and num <=2:
#         return (num -1)
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)

# num = 7
# print(fibonacci(num))

# def rev_number(n: str) -> str:
#     reversed_num = 0
    
#     while n != 0:
#         digit = n % 10
#         reversed_num = reversed_num * 10 + digit
#         n = n // 10
#     return reversed_num

# print(rev_number(12345))

# num = -123456
# print(str(num)[::-1])


from urllib.request import AbstractBasicAuthHandler


def palindrome(word):
    if len(word)%2 == 0:
        half_word = len(word)//2
        first_part = word[:half_word]
        second_part = word[half_word:]
        return first_part == second_part[::-1]
    else:
        return word[::-1]

word = "abba"
print(palindrome(word))

# def symmetry(word):
#     if len(word)%2 == 0:
#         half_word = len(word)//2
#         first_part = word[:half_word]
#         second_part = word[half_word:]
#         return first_part == second_part
#     else:
#         return False

# def check_word_palindrome_symmetry(word):
#     if palindrome(word) and symmetry(word):
#         print (f"{word} is both palindrome and symmetry")
#     elif palindrome(word):
#         print(f"{word} is a palindrome but not a symmetry")
#     elif symmetry(word):
#         print(f"{word} is a symmetry but not a palindrome")
#     else:
#         print(f"{word} is neither a palindrome nor a symmetry")

# word = "geynum"
# print(check_word_palindrome_symmetry(word))


from ast import Continue


# def reversed_number(num: int) -> int:

#     """Given a number, write a function to output its reverse digits. 
#     (e.g. given 123 the answer is 321) Make sure that if it is a negative 
#     number you keep the negative in the front (-123 becomes -321)
#     """
#     reversed_num = 0
#     negative = False

#     if num < 0:
#         negative = True
#         num = num * (-1)
    
#     while num != 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num = num // 10

#     if negative:
#         return reversed_num * (-1)    

#     return reversed_num



# number = -1236789766
# print(reversed_number(number))


# def fibonacci_without_recurssion(n: int) -> int:
#     n1 = 0
#     n2 = 0
#     iteration = 1
#     finbonacci_num = 0
    
#     while iteration < n:
#         iteration +=1
#         if iteration == 1:
#             continue
#         if iteration == 2:
#             finbonacci_num = 1
#             n2 = 1
#             continue

#         finbonacci_num = n2 + n1
#         n1 = n2
#         n2 = finbonacci_num
#     return finbonacci_num 

# n = 2
# print(fibonacci_without_recurssion(n))

# def rev_num(num: int) -> int:
#     num = str(num)
#     if num.startswith("-"):
#         num = num[1:]
#         return int("-" + "".join(reversed(num)))
#     return num[::-1]

# num = -10006
# print(rev_num(num))

numbers_in_hundred = str(list(range(1,101)))
#print(numbers_in_hundred)

split_num = numbers_in_hundred.split(",")
print(split_num)

normal_num = " +".join(split_num)
print(f"sum of numbers = {normal_num}")

def format_number(num: int) -> str: 
    return f'{num:,}'
    
             

number = 1000000
x = format_number(number)
print(x)


