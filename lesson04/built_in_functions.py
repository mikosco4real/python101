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

print( "add_5 =", add_5(7))

#Object Oriented Programming
class Student:
    def check_pass_fail(self):
        return self.marks >= 40
            
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 =Student("Harry", 85)


did_pass = student1.check_pass_fail()


print(did_pass)

student2 = Student("Janet", 30)

did_pass = student2.check_pass_fail()

print(did_pass)




class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def  add(self, number):
        real = self.real +number. real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result

n1 = Complex(5, 6)
n2 = Complex(-4, 2)

result = n1.add(n2)
print("Complex number =", result.real, result.imag)
print("imag =", result.imag)



class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self, b, c):
        result = self.a + b + c
        return result


t1 = Triangle(3, 4, 5)
t2 = Triangle(4, 5, 6)
perimeter_of_triangle = t1.perimeter(4,5)
perimeter_of_triangle2 = t2.perimeter(5,6)
print("The perimeter of triangle 1 =", perimeter_of_triangle)
print("The perimeter of triangle 2 =",perimeter_of_triangle2) 



class Even:
    def __init__(self, max):
        self.n = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
        return result

          

number = Even(10)
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))

import datetime as dt
class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd

        #Extract firstname and lastname from name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        today = dt.date.today()
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:])
        date_of_birth = dt.date(yyyy,mm,dd)
        age_in_days = (today - date_of_birth).days
        age_in_years = age_in_days/365
        return int(age_in_years)




user1 = User("Kelvin Michael", "19940620")
print(user1.last_name)

print(user1.age())



#Exception Handling in Python
for i in range(5):
    print("Hello world")

import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * math.pow(r,2)


radii = [2, 5, 7.1, 0.3, 10]

#method 1: Direct method 

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print (areas)

#method 2: map function

map(area, radii)
list_areas = list(map(area, radii))
print(list_areas)

#Example 2

temps_celsius = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("New York", 28), ("London", 22), ("Beijing", 32)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)
#This function is used to alter the evalues of individual items in the list or the tuples without changing the form of its construction
listed_farenheit = list(map(c_to_f, temps_celsius))
print(listed_farenheit)


#filter function

import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

filter(lambda x: x > avg, data)
#pass the filter function to a list constructor

above_avg = list(filter(lambda x: x > avg, data))
print(above_avg)
below_avg = list(filter(lambda x: x<avg, data))
print(below_avg)


#Remove missing data
countries = ["", "Argentina", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "","","Venezuela"]
#this function leaves only the desired data in te list by removing all the empty items in the list
complete_data = list(filter(None, countries))
print(complete_data)



#Reduce function
data1 = [2,3,5,7,11,13,17,19,23,29]
multiplier = lambda x, y: x*y
multiplied_data = reduce(multiplier, data1)
print(multiplied_data)

import math

def quadratic_formular(a=0, b=0, c=0):
    evaluate = math.sqrt(math.pow(b,2) - (4*a*c))
    x1 = (-b + evaluate) / (2*a)
    x2 = (-b - evaluate) / (2*a)
    return x1, x2


a = 2
b = 8
c = 4

solution = quadratic_formular(a, b, c)
print(f"{a}x2 + {b}x + {c} evaluates to x = {solution[0]:.2f} or x = {solution[1]:.2f}")

def force_impulse(m, v, u, t):
    final_momentum = m * v
    initial_momentum = m * u
    c_i_m = final_momentum - initial_momentum
    f = c_i_m / t
    return f


m = 50
v = 60
u = 40
t = 50

# impulse = force_impulse(m,v,u,t)
# print(f"The impulse is {int(impulse)}")



def fibonacci_without_recurssion(n: int) -> int: 
    fibonacci_number = 0
    first_number = 0
    second_number = 0
    iteration = 1

    while iteration < n:
        iteration += 1
        if iteration == 1:
            continue
        if iteration == 2:
            fibonacci_number = 1
            second_number = 1
            continue
        
        fibonacci_number = second_number + first_number
        first_number = second_number
        second_number = fibonacci_number

    return fibonacci_number


# nth_term = fibonacci_without_recurssion(1)
# print(nth_term)

numbers_hundred = list(range(1,101))
print(numbers_hundred)
numbers_split = str(numbers_hundred).split(",")
print(numbers_split)


import random
#display 10 random numbers from interval [0,1)
#Generate random numbers from interval [3,7)

def my_random():
    #Random, scale, shift, return...
    return 4*random.random() + 3

for i in range(6):
    print(random.randint(1,6))


outcome = ["rock", "paper", "scisscors"]

for i in range(10):
    print(random.choice(outcome))



# sums = []
#     s = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             s += arr[j]
#         s = s - arr[i]
#         sums.append(s)
#         s = 0
#     low = high = sums[1]
#     for i in range(len(sums)):
#         if low > sums[i]: 
#             low = sums[i]
#         if high < sums[i]:
#             high = sums[i]
#     print(low, high)
