
# usernames = "let us talk about the python language okay"
# string_usernames = list(usernames)
# capitalize_string = usernames.capitalize()

# length_of_string = len(usernames) #length of the string usernames
# #print(length_of_string)

# #To print out words with even length in the string 
# split_usernames = usernames.split(" ")

# def print_even_words(usernames):
#     for n in split_usernames:
#         if len(n)%2 == 0:
#             print(n)


# #print_even_words(usernames)
def print_even_words(words):
    for n in words.split(" "): # TODO: Use the argument you passed into the function
        if len(n)%2 == 0:
            print(n)

#print_even_words(usernames)

# #To find the number of characters in the string while ignoring spaces 
# new_username = "".join(usernames.split())

# length_username = len(new_username)
# #print(length_username)

# #To get find the unique chharacters in the string while ignoring spaces
# username1 = new_username

# unique_characters_set = set(username1)
# unique_characters1 = str(unique_characters_set)
# unique_characters = "".join(unique_characters_set)
# print(unique_characters)

# #Python program to check whether the string Palindrome or symmetrical
# #Check whether the string is Palindrome

def palin(string):
    st = 0         #declare and initialize with the starting and ending indices
    end = len(string) - 1
    f = 0  

#     #loop comparing letters moving from start to end and from end to start
#     while (st < end):
#         if (string[st] == string[end]):
#             st += 1
#             end -= 1
#         else:
#             f = 1
#             break
#     if f == 0:
#         print("The entered string is a palindrome.")
#     else:
#         print("The entered string is not a palindrome.")

# string1 = input("Enter the string: ")

# palin(string1)


# #Symmetrical function to check if string is symmetrical or not.
# def symm(string):
#     l = len(string)
#     flag = 0

#     if l % 2 == 0:
#         mid = l//2  #for even length 
#     else:
#         mid = l//2 + 1  #for odd length

#     s1 = 0 #starting for first portion of string
#     s2 = mid #starting for rest portion of string after middle value.

#     while (s1 < mid and s2 < l):
#         if (string[s1] == string[s2]):
#             s1 = s1 + 1
#             s2 = s2 + 1
#         else:
#             flag = 1
#             break


#     if flag == 0:
#         print("The entered string is symmetrical")
#     else:
#         print("The entered string is not symmetrical")
            
        

# string2 = input("Enter your string: ")

# symm(string2)

from asyncio.trsock import TransportSocket

# TODO: Improve this to be a function
# string3 = input("Enter a string of choice: ")

# def word_transform(string):
#     if len(string) < 3:
#         print(string)
#     elif string.endswith('ing'):
#         print(string + 'ly')
#     else: 
#         print(string + 'ing') 

# word = input("Enter a string of choice: ")
# word_transform(word)


# #To determine a duplicate value in a string

# def duplicate_letters(string):
#     word_list = string.split()
#     for word in word_list:
#         if len(list(word)) == len(set(word)):
#             return False
#         else:
#             return True

# string4 = input("Enter the string you wish to check: ")
# print([duplicate_letters(string4)])
# string4 = input("Enter the string you wish to check: ")
# print(duplicate_letters(string4))

def sum_digits(string):
    sum_digit = 0 
    for number in string:
        if number.isdigit() == True:
            z = int(number)
            sum_digit = sum_digit + z
            
    return sum_digit
    
string5 = "edfi3ij2lj4"

def palindrome(word: str) -> bool:
    if len(word) % 2 == 0:
        half_word = len(word)//2
        part1 = word[:half_word]
        part2 = word[half_word:]
        return part1 == part2[::-1]
    else:
        return word == word[::-1]

def symmetry(word: str) -> bool:
    if len(word) % 2 == 0:
        half_word = len(word)//2
        part1 = word[:half_word]
        part2 = word[half_word:]
        return part1 == part2
    else:
        return False

def checkword_for_sym_or_palin(word):
    if palindrome(word) and symmetry(word):
        return f"{word} is both palindrom and symmetry"
    elif palindrome(word):
        return f"{word} is a Palindrome but not a symmetry"
    elif symmetry(word):
        return f"{word} is a Symmetry but not a palindrome"
    else:
        return f"{word} is neither a symmetry or a palindrome"

print(checkword_for_sym_or_palin('wowwow'))
