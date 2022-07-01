# Variables in Python
name = "Michael Sage"
age = 30

# Container types in python
# list, tuples, set, dictionary, class objects

#list example
fruits = ["Mango", "Pineapple", "Apple"]

# List indexing
mango = fruits[0]
fruits[0] = "Mangoes"

# List Manipulation
fruits.append("Watermelon")
fruits.insert(0, "Gauva")

#tuples
# Diff tuples vs list is that tuples are immutable
subjects = ("Mathematics", "English", "Physics", "Chemistry")

#Set
# You can create sets with {} or set()

class_ids = {1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7, 7}

words = set(["Michael", "Michael", "Sage"])

fruits.append("Apple")
# print(fruits)

unique_fruits = set(fruits)
# print(unique_fruits)

# Dictionary
# Uses key, value pair

student1 = {"firstname": "Michael", "lastname": "Onwudufor", "age": 29, 
            "subjects": ["Maths", "Physics", "Chemistry", "English"]}

age = student1["age"]
chemistry = student1["subjects"][2]

# Dictionary operations
student1["age"] = 30
student1["class"] = "SS1A"


# Program flows
# if, if else, if elif else, for loop, while loop,

# 0-44 F, 45-54 P, 55-69 C, 70-100 A
score = 90

if (score >= 70 and score <= 100):
    print("Grade: A")
elif(score >= 55 and score < 70):
    print("Grade: C")
elif(score >= 45 and score < 55):
    print("Grade: P")
else:
    print("Grade: F")

#Functions
def sayHi(name):
    print("Hi " + name)

# sayHi("Michael")
# sayHi("Norbert")
# sayHi("Stanley")
# sayHi("Ender")
# sayHi("Fidelis")

# Nested if/else
# Functions in Python

usernames = ["sage", "mokolo", "favour"]
passwords = ['4getmen0t', 'yun0tm3', 'all0wm3']

def login(u, p):
    if (u in usernames):
        index_of_u = usernames.index(u)
        if (p == passwords[index_of_u]):
            print("Logged In successfully")
        else:
            print("Check your password and try again")
    else:
        print("Contact our admin to sign up")

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# login(username, password)

#While loop
print("While loop")
numbers = 0
while (numbers < 10):
    print(numbers)
    numbers += 1 # Equivalent to numbers = numbers + 1


# For loop
# Goes through iterables and does something.
for user in usernames:
    print(user)

#  Built in function - range
print("for loop")
for numbers in range(10):
    print(numbers)