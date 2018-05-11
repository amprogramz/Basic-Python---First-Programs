'''
This is based on the script from the video
"Learn Python in 60 Minutes from Java"
by Krohn - Education
https://www.youtube.com/watch?v=xLovcfIugy8

I personally feel like this was a great video, and this script pretty much covers the basics of using Python for any
one who has predominately used Java.
'''

print("hello " + "world")

# single line coment
'''
multi
line 
coment
'''

# Var assignments do not need to define type
x = 4
print("x =", x)
# Addition, sep defines spacing after comma.
x = 4 + 4
print("x = ", x, sep="")
# 2 to the 3rd power
x = 2**3
print("x =", x)
# Type casting
x = int(3.5)
print("x =", x)
# max min
x = max(3, 4)
print("x =", x)


'''
# Taking user input
print("Please enter a number:")
x = input()
print("You entered:", x)
# or
x = input("Please enter a number:\n")
print("You entered:", x)
# or with a cast
x = float(input("Please enter a number:"))
print("You entered:", x)
#'''

# Sting length
n = "word"
print(n)
print("String length:", len(n))
# substring
print("Substring 1:", n[1:3])
# substring last 3
print("Substring 2:", n[-3:])
# contains
print("Contains:", ("ord" in n))


# Arays
list = []

list.append("webo")
list.append("mantequilla")
list.append("tomates")

print("list:", list)
print("list length:", len(list))
print("list index1:", list[1])
# add remove at specific index
list.insert(1, "eggs")
print(list)
del(list[1])
print(list)
# select index range, index 1 & 2 int this example
print(list[1:3])
# new list
list2 = []
list2.append("eggs")
list2.append("butter")
list2.append("tomatoes")
# combine two lists
list3 = list + list2
print(list3)
# multidimensional array
list4 = []
list4.append(list)
list4.append(list2)
print(list4)
print(list4[0][2])
# Tuple, like an array but is final
list5 = 1, 2, 3, 4, 5, 6
print(list5)
print(list5[1])
# Tuple no no, list5.append(7)
print(list5)
# Tuple search
print(5 in list5)


# Operators
# equals
var1 = "" #input()
var2 = "house"
# checks if equal
print(var1 == var2)
# checks if same instance
print(var1 is var2)
# Python uses ==, <, >, <=, >= like Java
# Python uses not, and, or as a word instead of ! && ||

'''
# If statements, and while loop example
var = 0
varCount = 0

while var < 1 or var > 5:
    var = int(input("enter a number between 1 and 5:"))
    varCount += 1
    if var == 1:
        print("entered 1")
        print("You took", varCount, "attempts")
    elif var == 2:
        print("entered 2")
        print("You took", varCount, "attempts")
    elif var >= 3 and var <= 5:
        print("entered a number between 3 and 5")
        print("You took", varCount, "attempts")
    else:
        print("Error, should have entered a number between 1 and 5...")
        print("attempt", varCount)
#'''

# for loops
for index in range(10):
    print(index, end=" ")

print(" ")
for index in range(1, 11):
    print(index, end=" ")

print(" ")
for index in range(1, 11, 2):
    print(index, end=" ")

# New for loop like Java
print(" ")
array = [1, 2, 3, 4, 1]
for index in array:
    print(index, end=" ")

print()
for index in array:
    if index == 3:
        break
    print(index, end=" ")

print()
for index in array:
    if index == 3:
        continue
    print(index, end=" ")

# else entered
print()
for index in array:
    print(index, end=" ")
    if index == 5:
        print("break")
        break
else:
    print("else entered")

#else not entered
#print()
for index in array:
    print(index, end=" ")
    if index == 3:
        print("break")
        break
else:
    print("else entered")


# Functions
def sum(a, b, c):
    return a + b + c


# Python allows user to assign function to a variable name.
mystery = sum

print(sum(1, 1, 3))
print(mystery(1, 1, 3))


# Ability to default instead of overloading
def sumIt(a, b, c=0, d=0, e=0, f=0):
    return a + b + c + d + e + f


print(sumIt(1, 2))
print(sumIt(1, 2, 3, 4, 5, 6))


class Dog:

    # constructor, _ makes var private, self
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    # This basically becomes a static method when it dose'nt include self
    def random(a):
        return 7 + a

    def __str__(self):
        return "Dog:\nName: " + self._name + "\nAge: " + str(self._age)


d1 = Dog("Scruffy", 5)
print()
print(d1)
print(Dog.random(1))




