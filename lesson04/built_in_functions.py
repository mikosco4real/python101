 # Datetime
# Timedelta
# functools
# map
# reduce
# product
# lambda
# os
# enumerate
# zip
# eval
# sorted
# abs
# min
# max
# Random

# File Handling
# CSV

from datetime import datetime

from datetime import timezone
from itertools import product
from unittest.util import three_way_cmp

current_time = datetime.now()

date_time_format = datetime.strftime(current_time, " %A, %B %d, %Y")

today = '06-09-2022'

parse_date_time = datetime.strptime(today, "%d-%m-%Y")

#########################
from datetime import timedelta

yesterday = datetime.date(datetime.strptime('05/09/2022', '%d/%m/%Y'))
today = datetime.date(datetime.today())

start_exam = datetime.now()

# time allowed for this exam is 40 mins

end_exam = start_exam + timedelta(minutes=40)


from functools import partial, reduce


def add(a, b):
    return a + b

def solve(a, b, c):
    return True


add_5 = partial(add, 5)

def hello1(name):
    print("Hello "+ name)

# Lambda
hello = lambda name: print("Hello " + name)

# Map, Reduce, Product

num = [1,2,3,4,5,6]
num2 = [5,6,7,8,9,10]

# print(list(map(lambda x: x ** 2, num)))

# print(list(product(num, num2)))

# print(reduce(lambda x,y: x+y, num))


# Enumerate, Zip

iter1 = [1,2,3,4,5]
iter2 = [6,7,8,9,10]
# print(list(zip(iter1, iter2)))

firstname = ["Michael", "David", "Jude"]
lastname = ["Sage", "Onwudufor", "Okeke", "Okolo"]

# for f, l in zip(firstname, lastname):
#     print(f,l)


fruits = ["apple", "banana", "mango", "paw paw", "pineapple"]

# for i in range(len(fruits)):
#     print(f"{i+1}. {fruits[i]}")

# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}. {fruit}")

# The spread operator *

def say_hi(firstname, lastname):
    print(f"Hello {firstname}, {lastname}. How are you?")

name1 = ["Michael", "Okolo"]
name2 = ["Ender", "Onwudufor"]
name3 = ["Sage", "Michael"]

say_hi(*name1)
say_hi(*name2)
say_hi(name3[0], name3[1])
