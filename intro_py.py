integer = -3
v_float = 1.5
string = "testing py one more time"

type(integer)
type(v_float)
type(string)

age = int(input("How old are you?")) #int to control format type
age

type(age)

winter = "cold"

test = winter.upper()
test

test = winter[1:]
test

test = winter.replace("c","m")
test

winter.find("l")
winter.find("g")

len(winter)

n1 = 14
n2 = 16

n1/n2
print(f"Division of {n1} by {n2} is {n1/n2}")

def consume_liters(time, velocity):
    distance = time*velocity

    liters = round(distance/12,2)
    return liters


consume_liters(5,85)

def marriage(person1,person2):
    if person1 == person2 and person1 == True:
        result = "Congratulations!"
    else:
        result = "Try again."
    return result

marriage(False,False)

def oldest(age1,age2):
    if age1 > age2:
        result = age1
    elif age1 < age2:
        result = age2
    else:
        result = "the same age"
    return print("The oldest one is",result)

oldest(21,21)

import statistics
def class_approval(m1,m2,m3):
    grade = statistics.mean([m1,m2,m3])

    if grade >= 0 and grade <= 4:
        result = "Failed."
    elif grade > 4 and grade <= 6:
        result = "Failed but you can try the second chance exam."
    elif grade > 6:
        result = "Approved!"
    
    return result

class_approval(8,5,4)

for numero in range(1,10):
    print(numero**2//2)

numero = 0
while numero <= 10:
    print(f"3*{numero} = {3*numero}")
    numero += 1

sexuality = ("Hetero","Homo","Bi","Asexual")
sexuality[1]
type(sexuality)

students = ["Maria","John","Stuart"]
students.append("Peter")
students

student_grade = {"Maria" : 9.5,
                 "John"  : 6.6,
                 "Stuart": 8,
                 "Peter" : 4}

student_grade
del(student_grade)["Peter"]
student_grade

student_grade.values()
student_grade.keys()

colors = ["blue","yellow","pink","red","pink","yellow","yellow","yellow","green"]
set(colors)

#pip install numpy
import numpy as np
matrix = np.array([[2,2,3],[4,4,5]])
matrix
matrix[0][2]

def happy_birth(person):
    print(f"Happy birthday {person}!")
happy_birth("Maria")

for names in ["Maria","John","Stuart"]:
    happy_birth(names)

def celsius_to_fahrenheit(celsius):
    return (9*celsius + 160)/5

celsius_to_fahrenheit(-10)

#pip install datetime
#pip install math
#pip install random
#pip install time

import datetime
import math
import random
import time as tm

random.random()

before = tm.time()

for number in range(0,10):
    print(number)

tm.sleep(2)
after = tm.time()

print(f"Time used {after - before}")

list = ["10",9.5]

try:
    list[1]/list[0]
except ZeroDivisionError:
    print("It's not possible to divide by 0.")
except IndexError:
    print("Invalid list value.")
except KeyboardInterrupt:
    print("Interrupted")
except TypeError:
    print("Invalid value.")



with open("text.txt") as text:
    for line in text:
        print(line)

with open("text.txt") as text:
    r = text.readlines()
r

student_grade = {"Maria" : 9.5,
                 "John"  : 6.6,
                 "Stuart": 8,
                 "Peter" : 4}

with open("text_grades.txt", mode="w") as txt_grades:
    for student, grade in student_grade.items():
        txt_grades.write(f"The student {student} got a {grade} in Math class.\n")



import re

frase = "Hello, my mobile is +55(21)90000-0000"

re.search("\+\d{2}\(\d{2}\)\d{4,5}-\d{4}",frase)

car = "My car is BRB-1997"

re.search("[A-Z]{3}-\d{4}",car)

car2 = '''BRB-1997 is my car. USA-1998 is my car. CUB-1999 is my car'''

re.match("[A-Z]{3}-\d{4}",car2)

re.findall("[A-Z]{3}-\d{4}",car2)

parque_lage = "Endereço: R. Jardim Botânico, 414 - Jardim Botânico, Rio de Janeiro - RJ, 22461-000. Para saber mais, procure no www.google.com"

re.search("\d{5}-\d{3}",parque_lage) #cep

re.search("\d{3}",parque_lage) #numero

re.search("\w+\.\w+\.com",parque_lage) #url

class triangle:
    def __init__(self, side1,side2,side3, base, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.height = height
    
    def area (self):
        return (self.base*self.height)/2
    
    def type_tri(self):
        if self.side1 > self.side2 + self.side3:
            return "It's not a triangle"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "It's an isoceles triangle"
        else:
            return "Type of triangle not identified"

tri1 = triangle(2,1,3, base=4, height=3)
tri1.side1
tri1.base

tri1.area()
tri1.type_tri()
type(tri1)