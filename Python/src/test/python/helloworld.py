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
# Taking user in
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
# tuple search
print(5 in list5)


