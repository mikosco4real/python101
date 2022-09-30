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
