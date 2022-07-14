
usernames = "let us talk about the python language okay"
string_usernames = list(usernames)
capitalize_string = usernames.capitalize()

length_of_string = len(usernames) #length of the string usernames
#print(length_of_string)

#To print out words with even length in the string 
split_usernames = usernames.split(" ")

def print_even_words(usernames):
    for n in split_usernames:
        if len(n)%2 == 0:
            print(n)


#print_even_words(usernames)

#To find the number of characters in the string while ignoring spaces 
new_username = "".join(usernames.split())

length_username = len(new_username)
#print(length_username)

#To get find the unique chharacters in the string while ignoring spaces
username1 = new_username

unique_characters_set = set(username1)
unique_characters1 = str(unique_characters_set)
unique_characters = "".join(unique_characters1.split())
#print(unique_characters)

#Python program to check whether the string Palindrome or symmetrical
#Check whether the string is Palindrome


def palin(string):
    st = 0         #declare and initialize with the starting and ending indices
    end = len(string) - 1
    f = 0  

    #loop comparing letters moving from start to end and from end to start
    while (st < end):
        if (string[st] == string[end]):
            st += 1
            end -= 1
        else:
            f = 1
            break
    if f == 0:
        print("The entered string is a palindrome.")
    else:
        print("The entered string is not a palindrome.")

string1 = input("Enter the string: ")

palin(string1)


#Symmetrical function to check if string is symmetrical or not.
def symm(string):
    l = len(string)
    flag = 0

    if l % 2 == 0:
        mid = l//2  #for even length 
    else:
        mid = l//2 + 1  #for odd length

    s1 = 0 #starting for first portion of string
    s2 = mid #starting for rest portion of string after middle value.

    while (s1 < mid and s2 < l):
        if (string[s1] == string[s2]):
            s1 = s1 + 1
            s2 = s2 + 1
        else:
            flag = 1
            break


    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
            
        

string2 = input("Enter your string: ")

symm(string2)



string3 = input("Enter a string of choice: ")

if len(string3) < 3:
    print("String is less than 3 characters")
elif string3.endswith('ing'):
    print(string3 + 'ly')
else: 
    print(string3 + 'ing') 


#To determine a duplicate value in a string

def duplicate_letters(string):
    word_list = string.split()
    for word in word_list:
        if len(word) == len(set(word)):
            return False
        else:
            return True

string4 = input("Enter the string you wish to check: ")
duplicate_letters(string4)

