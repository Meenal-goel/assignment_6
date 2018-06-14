#1- Take 10 integers from user and print it on screen.

#create an empty list for adding user input in future
ele_list = []
print("enter the integers")
#take integers from user input
for i in range(10):
    val = input()
    #store the input in list using append function
    ele_list.append(val)
print(ele_list)
print("the user input is:")
#display the user input which are now the list elements
for j in ele_list:
    print(j)
print("\n")

#2- Write an infinite loop.An infinite loop never ends. Condition is always true.

'''var=5
while (var > 0):
    print("infinite loop")
    
print("\n")'''

#3-Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

#create an empty list for adding user input in future
elm_list = []
#create an empty list for adding square of elements of elm_list
sq_list = []
print("enter list elements")
#take user input
for x in range(6):
    num=input()
    #store the input in list using append function
    elm_list.append(num)
print("our first list is:")
print(elm_list)
for x in elm_list:
    #compute square of the elements present in elm_list
    x = (int(x)*int(x))
    #store the square of each element in list named sq_list
    sq_list.append(x)
print("the list having square of elements present in first list is:")
print(sq_list)

print("\n")

#4- From a list containing ints, strings and floats, make three lists to store them separately

integer_list = []
strings_list = []
floats_list = []
mix_list = [4, 'table', 1.1, 'chair', 2, 5, 'sofa', 1.1, 'bed', 2.5]


for each_elem in mix_list:
    #check for integer type element
    if(type(each_elem) == int ):
        i1 = each_elem
        integer_list.append(i1)
    #check for string type element
    elif(type(each_elem) == str):
        s1 = each_elem
        strings_list.append(s1)
    #heck for float type element
    elif(type(each_elem) == float):
        f1 = each_elem
        floats_list.append(f1)
print("list of integer type elements:",integer_list)   
print("list of string type elements:",strings_list)    
print("list of float type elements:",floats_list)

print("\n")

#5-Using range(1,101), make a list containing even and odd numbers.

evn_list = []
odd_list = []

for every_elem in range(1,101):
    if(every_elem % 2 == 0):
        num=every_elem
        evn_list.append(num)

    else:
        num=every_elem
        odd_list.append(num)
print("list containing even numbers :",evn_list)
print("list containing odd numbers :",odd_list)
            
print("\n")

#6-Print the following patterns: 
# *
# **
# ***
# ****
# (note that '#' in above lines is used to denote comment ,they are not included in pattern)

pattern_list = [1,2,3,4]
for sym in pattern_list :
    print(("*")*sym)

print("\n")

#7-Create a user defined dictionary and get keys corresponding to the value using for loop.

user_dict = {}
n=int(input("enter the number of elements to be present in dictionary:"))
for every_n in range(n):
      k = input().split()     #split the input text based on space & store in the list k
      user_dict[k[0]] = k[1] 
    
print(user_dict)
for k,v in user_dict.items():
    print (k,v)

print("\n")



#8-Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

e_list = []
print("enter the list size")
size=int(input())
print("enter the list elements")
#take integers from user input
for element in range(size):
    z= int(input())
    #store the input in list using append function
    e_list.append(z)
print("Initially list is :",e_list)
print("enter the element to be searched")
my_key=int(input())
for each_element in e_list:
    if(  my_key == each_element):
        print("element found")
        print("element to be popped is ",each_element)
        e_list.remove(each_element)
     
        print("updated list is:",e_list)

