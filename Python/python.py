# Input text
str1 = input('please input first name:')
str2 = input('please input last name:')
print("Hello" + str1 +" "+str2)

#If Function
bill_total = 295
discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100!")
    bill_total = bill_total - discount1
elif bill_total > 200:
    print("Bill is greater than 200!")
    bill_total = bill_total - discount2
else:
    print("Bill is less than 100!")
print("Total bill is: " + str(bill_total))

#Switch Statement
http_status = 500

if http_status == 200 or http_status == 201:
    print("Success")
elif http_status == 400:
    print("Bad request")
elif http_status == 404:
    print("Not Found")
elif http_status == 500 or http_status ==501:
    print("Server Error")
else:
    print("Unknown")

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown") 

#Looping - For Loop
for i in range(10):
    print("Looping", i)

favourites = ['creme Brulee', "Apple Pie", "Churros", "Tiramisu", "Chocolate cake"]
for item in favourites:
    print("I like desserts", item)

#Looping - While Loop
favourites = ['creme Brulee', "Apple Pie", "Churros", "Tiramisu", "Chocolate cake"]
count = 0
while count < len(favourites):
    print("I like desserts", favourites[count])
    count +=1

#Function
def calculate_tax(bill, tax_rate):
    return (bill * tax_rate)/100

print("Total tax is", calculate_tax(175,7.5))

#Local and Global Scope
my_global = 10

def fn1():
    enclosed_v = 8
    def fn2():
            local_v = 5
            print("access global state: ", my_global)
            print("access to enclosed: ", enclosed_v)
            print("access to local: ", local_v)
    fn2()
fn1()

# List are mutable: can be changed
my_list =[1, 'strings', 4.5, True]
print(my_list[1])
print(type(my_list))
my_list[0] = 5
print(my_list.index(4.5))
my_list.append(10)
for x in my_list:
    print(x)

# Turples are immutable: cannot be changed
my_turple = (1, 'strings', 4.5, True)
print(my_turple[1])
print(type(my_turple))
print(my_turple.index(4.5))
for x in my_turple:
    print(x)

# Sets don't allow duplicate values & it doesn't work with index
set_a = {1,2,2,3,3,3,4,5,6,7}
set_a.add(8)
set_a.remove(2)
set_a.discard(3)
print(set_a)

set_a={1,2,3,4,5}
set_b ={4,5,6,7,8,9,10}
print(set_a.union(set_b))
print(set_a | set_b)

print(set_a.intersection(set_b))
print(set_a & set_b)

print(set_a.difference(set_b))
print(set_a - set_b)

print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)
  
# Dictionary has keys and values but does not allow duplicate keys.
sample_dict = {1: 'coffee', 2: 'Tea', 3: 'Juice'}

print(type(sample_dict))
print(sample_dict[1])

sample_dict[2] = " Chocolate"
print(sample_dict)

del sample_dict[3]
print(sample_dict)

for x in sample_dict:
    print(x)    
for key, value in sample_dict.items():
    print("I love " + str(key)+ " " + value)

# *args
def sum_of(a,b,c):
    return (a+b+c)
print(sum_of(4,5,6))

def sum_off(*args):
    sum = 0
    for x in args:
        sum+=x
    return sum
print(sum_off(4,5,6,5))

# *kwargs
def sum_of(**kwargs):
    sum=0
    for k, v in kwargs.items():
        sum+=v
    return round(sum, 2)
print(sum_of(coffee= 45.59, tea = 20.52, juice = 33.88))

#Handling Exceptions by printing error
def divide_by(a,b):
    return a/b
try:
    print(divide_by(40,0))
    
except ZeroDivisionError as e:
    print(e, "Cannot divide by zero")

except Exception as e:
    print("Something went wrong!",e)
    print(e.__class__)

# Sorted Functions
coffees =["Espresso", "Lattle", "Cappuccino", "Macchiato", "Americano", "Decaf"]
print(sorted(coffees))

def reverse(str):
    return str[::-1]
reserved_coffees = map(reverse, coffees)
for x in reserved_coffees:
    print(x)

#Pure Functions
my_list=[1,2,3]
def add_to_list(lst, item):
    nl=lst.copy()
    nl.append(item)
    return nl
new_list = add_to_list(my_list,4)
print(new_list)

#Recursion
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(5))

#Reversing in Python
trial ="reversal"
new_trial = trial[::-1]
print(new_trial)

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
reverse = string_reverse(trial)
print(reverse)

#Map and Filter
menu =["Espresso", "Lattle", "cappuccino", "Macchiato", "Americano", "Decaf"]

def find_coffee(coffee):
    if coffee[0] == "L":
        return coffee
    
map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)

#Classes
class Myclass:
    a = 5
    print("Hello")

    def hello(selsf):
        print("Hello, world!")
myc = Myclass()
print(myc.a)
print(myc.hello())

#Classes OOP
class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare")

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 45)

print(pizza.items)
print(pizza.dish)
print(pizza.time)

print(pizza.contents())

#Instance Method
class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    def pay(self):
        self.payment = "yes"
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid" + str(self.amount)
        else:
            return self.name + " is not paid yet"
nathan = Payslips("Nathan", "yes", 2000)
roger = Payslips("Roger", "no", 3000)
print(nathan.status(), "\n", roger.status())

#Parent and Child classes
class Employees:
    def __init__(self,name, last) -> None:
        self.name = name
        self.last = last
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
class Chefs(Employees):
    def leave_request(self, days):
        return("May I take a leave for ", str(days) + " days")
adrian = Supervisors("Adrian", "A", "apple")
emily = Chefs("Emily", "E")
juno = Chefs("juno", "j")
print(emily.leave_request(3))
print(adrian.password)
print(emily.name)
    
#Accessing Modules
import sys
locations = sys.path
print(locations)
for i in locations:
    print(i)

import calendar
leapdays = calendar.leapdays(2000, 2050)
isitleap = calendar.isleap(2036)
print(leapdays)
print(isitleap)

import math
root = math.sqrt(9)
print(root)
from math import sqrt
root = sqrt(9)
print(root)
import math as m
const = m.cos(0)
print(const)
from math import factorial as f
factorial_10 = f(10)
print(factorial_10)
from math import *
x = log10(50)
print(x)

# Scoping
def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("inside nested function " + animal)
    print("Before calling function" + animal)
    e()
    print("After nested function " + animal)
animal = "camel"
d()
print("Global animal " + animal)

import importlib
import name
def changesFile():
    importlib.reload(name)
    name.changes()
for i in range(2):
    changesFile()

#FullStack Framework
    #Form Generators
    #Template Layouts
    #HTTP Request Handling
    #WSGI interfaces
    #Database Connection Handling
#Python Framework
    #Django
    #Web2py
    #Pyramid
#Micro Framework
    #Flask
    #Bottle
    #Dash
    #CherryPi