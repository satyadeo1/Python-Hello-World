# -*- coding: utf-8 -*-
"""
Python keywords
"""

import keyword
keyword.kwlist
################################

10+10

x = pow(2,10);
x;
print(x);

sum1=10+10;
sum1;
#len(sum1);

################################
#Data Type
#Booleans => Y/N/True/False/0/1
#String =>'a', 'A', 'Hello'
#'Hi I am Working as Python Programmer'
#"A"

PK='A'
type(PK)

#List >[]

#List > []

listOne = list([1,2,[1.1,2.2]]);
listOne;
type(listOne)
len(listOne);

#accessing element of nested list = first element of sub list 1.1
listOne[2][0]

listOne1 = ['A', 'Hello',11,1.2];
listOne1;

# Extend List
L1=['a','b'];
L2=[1,2];
L3=['Java', 'Python'];
L1+L2+L3;

# extend () to add two list
A1 = [ 'a', 'b'];
A2 = ['c', 'd'];
A1.extend(A2);
print(A2);
print(A1);

# Append() ; will create nested list
B1 = ['Hi', 'HELLO'];
B2 = [1,2];
B1.append(B2);
print(B1);

# Delete List
##### Delete Element  - value needs to be provided for deletion#####
elm = ['a', 'b', 'c','d','e'];
elm.remove('e');
print(elm);

#remove by position
elm = ['a', 'b', 'c','d','e'];
elm.pop(1);
print(elm);

# remove last position
elm = ['a', 'b', 'c','d','e'];
elm.pop();
print(elm);

# clear all elements from list
elm = ['a', 'b', 'c','d','e'];
elm.clear();
print(elm);

# Sort elements of a  list
elm = ['a', 'c', 'b','d','e'];
elm.sort();
print(elm);

# Reversing the sequence of elements
elm = ['a', 'b', 'c','d','e'];
elm.reverse();
print(elm);

# Findng first index position of n element in a List
elm = ['a', 'b', 'c','d','e'];
i = elm.index('b');
print(i);

################## String ##################

v1 = 'a'
v2 = "A"
v3 = """A"""
print(v1);
print(v2);
print(v3);
type(v1);

# """ is required when we need multiple lines as string
v4 = """ wdhiudhef
dwcgfvhcfweu
bhdsbwiud"""
print(v4);

v5 = "PYTHON";
v5[-2]
v5[2]

#v5[2] = 'B' #TypeError: 'str' object does not support item assignment

###
#V1[3:5]------[Start Include: End Exclude]
v1 = "PYTHON String"
v1[-1];
len(v1);
#v1[13]; - #IndexError: string index out of range
print(v1);
v1[3:5]; #this will give o/p 'ho'
print(v1);
print(v1[-1:-7])

v1 = "PYTHON String"
print(v1[-1:-7])
print(v1[-7:-1])
print(v1[-7:])
print(v1[-6:])


L1 = [1,2,3,4,5,6,7]
print(L1[1:4])
print(L1[-1:-4])
print(L1[-4:-3])
print(L1[-4:])
print(L1[6:])
print(L1[-4:-2])
print(L1[-4:-1])
print(L1[-4:0])
print(L1[-4:1])
print(L1[-4:2])
print(L1[2:-4])
print(L1[3:-4])

#####################################################
v1 = "PYTHON String"
print(v1[7:9])
print(v1[7:-4])
print(v1[-6:-4])

v1 = "PYTHON String"
#v1[2] = 'b' # will give error because String doesn't allow element update. String is immutable
# Deleting element from string from specific position is not possible.

del v1; # can delete whole string

######################## String Operations #############################

var1 = "Python"
var2 = "String"

print(var1+var2) #it will create another variable with combined string "PythonString"
print(var1*3) # gives same value three times "PythonPythonPython"
#print(var1/3) # DOESNOT work because it means changing element of string

print('t' in var1) # to validate if a character is present in a string. o/p - True or False. CASE SENSITIVE
print('T' in var1) # to validate if a character is present in a string. o/p - True or False. CASE SENSITIVE
print('t' not in var1) # to validate if a character is NOT present in a string. o/p - True or False. CASE SENSITIVE

#isupper(),islower(),lower() ----to check upper or lower case characters

print(var1.isupper()); # o/p TRUE or FALSE
print(var1.islower()); # o/p TRUE or FALSE
print(var1.lower()); # to change all characters in lower case
print(var1.upper()); # to change all characters in upper case

####################### LOOPS ###########################################
#For Loop
for val in var1:
    print(val)    #This will print all characters one by one in new line each

for val in 'Python String':
    print(val)

#If Else Loop
a=3;
if (a==2):
    print(a) #Indentation is very important. Shouldn't change start location of print or else statements
else:
    print("hi")

for x in var1:
    print(x)

# r or R to skip escape characters
print (r'\n')
print(R'\n')

#r'c:/abc/xyz/temp/test.csv'

# print("Python is used in machine learning application and it is "GOOD"") # will throw error' invalid syntax'

print("Python is used in machine learning application and it is \"GOOD\"") #use of \

###### Format String ######
print("Name:", 'ABC')
print("Name:", 'ABC', 25)
print("Name:%s, \n Age: %d" % ('ABC', 25))

##

for val in 'Python String Test':
    print(val)

# for loop with indent
for x in [1,2,3,4,5,6]:
    print(x)
    print('Test1')
    print('Test2')

# for loop without indent
for x in [1,2,3,4,5,6]:
    print(x)

print('Test1')
print('Test2')

## If condition with indentation
x=2;
if (x==2):
    print('Value maches')

#################################
arr = [1,2,3,4,5,6]
print(arr[2]) # no : means index
print(arr[2:3]) # : means split
print(arr[2:4:-1])
print(arr[::-1])

################################## SET ##################################################
# Set : don't have specific order
# Set : position can be insonsistent
# Set : will have unique item or can't have duplicate items
# Set : Items / elements are immutable
# Set : set is itself mutable & allows additions or deletion of items

# {11,12,[1,2,3]}
# {} or set()
# Examples of set

myset = {3,7,13,15}
print(myset)
type (myset)
len (myset)
#myset[3] # wouldn't allow this as set elements are imutable

#myset1 = set {1,1.1, 'A', [12,12,14,15]} #throws exception

#myset1 = {11,1.1, "A" [12,12,14,15]} #throws exception

s1 =  {1,(2,3,4)}
s2 = set (["A", "B", "C"])

L11 = ["A", "B", "C"]
s12 = set(L11)

# Add and update two sets
s1 = {1,(2,3,4)}
s2 = set (["A", "B", "C"])

#s3 = s1.add(s2)
s4 = s1.update([44,45,46])
print(s4)
print(s12.update([44,45]))

####### Remove from a set # .discard() or .remove() or .pop() or .clear()
s12.discard("AA")
#s12.remove("AA")
#s12.pop("AA")
s12.pop()
s12.clear()

#Example---Union |

setA = {'a','e','i','o','u','g','h'}
setB = {'a','e','z','b','t','o','u'}
print(setA)
print(setB)

print(setA | setB) #union of setA and setB
print(setA.union(setB)) #union of setA and setB

#Example--- Intersection &
setA = {'a','e','i','o','u','g','h'}
setB = {'a','e','z','b','t','o','u'}

print(setA & setB) #Intersection of setA and setB
print(setA.intersection(setB)) #Intersection of setA and setB

# For loop in set
for elm in setA:
    print(elm)

## For loop with if condition
for elm in setA:
    print(elm)
    if ('u'==elm):
        print("got the value: ",elm)

################################## TUPLE ##################################################
# tuple: immutable
# tuple: sequence
# tuple: heterogeneous
# tuple: ()

# tuple creation one way
mytuple1 = (33,55,77)
print(mytuple1)

# tuple creation another way
mytuple2 = 33,44,55
print(mytuple2)

# functions on tuple
type(mytuple1)
len(mytuple1)
mytuple1[0]
mytuple1[1]

#heterogeneous
hetroTuple1 = (22,"22",[3,3,4])
print(hetroTuple1)

print(hetroTuple1[2]) # Index is allowed in tuple
print(hetroTuple1[-2]) # Index is allowed in tuple

print(hetroTuple1[2:]) # Slice is allowed in tuple

#hetroTuple1[2] = 1 # immutable so not allowed - TypeError: 'tuple' object does not support item assignment

hetroTuple1[2][1] = 4 # manipulating list under tuple works

#del
#del hetroTuple1[2] # immutable so not allowed - TypeError: 'tuple' object doesn't support item deletion
del hetroTuple1 # deletion of whole tuple works


################################## DICTIONARY ##################################################
# Dictionary : {} like d1 = {} or d1 = {key:Value}
# Dictionary : key should be unique but values can be duplicate
# Dictionary : key value pair where unique key an have multiple values
# Dictionary : this data type is used where need 2 level of access is required? like Key1=username and key2= password

v1 = {}
type(v1) # o/p will be dict

mydct = {1:"A"} # here key is 1 and value is 'A'
print(mydct)

mydct2 = {1:"A",2:"B",3:"C"}
print(mydct2)
print(mydct2[2])

mydct3 = {'studentName':"Satya", 'Roll':123, 'Sub':'Programming'}
print(mydct3)
print(mydct3['studentName'])
mydct3['exam'] = 'Online' # addition of new elment in dictionary
mydct3['exam'] = 'offline' # updation of new elment in dictionary

del mydct3['exam'] # deletion of an element from dictionary

# Unique key and duplicate values allowed
mydct3['exam1'] = 'Online'
mydct3['exam2'] = 'offline'
mydct3['exam3'] = 'offline'
type (mydct3) # o/p will be 'dict'

##
# different ways of creating dictionary
num_dict = {1:'cricket',2:'baseball'}
print(num_dict)

mydict = dict({1:'veg',2:'non-veg'})
print(mydict)

mydict_tuple = dict([(1,'pune'),(2,'mumbai')]) # dict creation using tuple
print(mydict_tuple)

# Examples
satyadct1 = {'Name':"Satya", 'Roll':123, 'Sub':'Programming'} # Mix data dict
print(satyadct1)
print(satyadct1['Name']) #Access elements by Key
satyadct1['city'] = 'pune' # adding parameters to dictionary
satyadct1['Roll'] = 111 # updating value
satyadct1['city'] = 'pune', 'mumbai' #multiple values to one single key

city = ('pune', 'mumbai', 'delhi')
satyadct2 = {'Name':"Satya", 'Roll':123, 'Sub':'Programming', 'city':['pune', 'mumbai', 'delhi']}# list in a dictionary
print(satyadct2)
satyadct2['city'][2] = 'kolkata'

#.del
#.pop

satyadct2 = {'Name':"Satya", 'Roll':123, 'Sub':'Programming', 'city':['pune', 'mumbai', 'delhi']}
print(satyadct2)
# print all keys in a dictionary
print("All Keys in dict satyadct2 are: ")
for key in satyadct2:
    print(key)

# print key & values through iteration ----dict without a list
satyadct1 = {'Name':"Satya", 'Roll':123, 'Sub':'Programming'}
print("{keys}:{Values}")
for key, value in satyadct1.items():
    print({key}, ":", {value})

satyadct2 = {'Name':"Satya", 'Roll':123, 'Sub':'Programming', 'city':['pune', 'mumbai', 'delhi']}

# print key & values through iteration ----dict with a list
satyadct2 = {'Name':"Satya", 'Roll':123, 'Sub':'Programming', 'city':['pune', 'mumbai', 'delhi']}
#{city}:{['pune', 'mumbai', 'delhi']}
print("{keys}:{Values}")
for key, value in satyadct2.items():
    print(key, ":", value)

###### dict creation through list
days = ['sun','mon','tue','wed','thu','fri','sat'] #List
type(days)
{day:len(day) for day in days}

# dictionary comprehensation
{day: i for i, day in enumerate(days)} # Iterat / assign day number to the values  / create a sequence of elements

# List comprehensation
range(5)
[lst for lst in range(5)] # creating dict from a list in a single line

#Example2
listcity = ["pune", "mumbai", "Nashik","Nagpur"]

[city[0] for city in listcity] # gives first letter of each element from list
[city[-1] for city in listcity] # gives last letter of each element from list
#[if (city[0]==N) for city in listcity] ?????? If loop to be covered later

# for loop doesn't check any condition, While loop checks condition and then iterates

#while some condition:
#    print();
#example of while loop
x = 4
y = 3
while x>y:
    print(y)
    break

while x<y:
    print(y)
    break

# same can be achieved in For loop using if inside for - to compare or put a condition

# If Statement
a = 33
b = 100

if b > a:
    print(b)

# Elif - if previous statement is not true then check another condition and continue ;

a = 33
b = 33
if b > a:
    print("b is greater")
elif a == b:
    print("Equal")

# If else statement - else is the final check

a = 1000
b = 11
if b > a:
    print("b is greater")
elif a == b:
    print("Equal")
else:
    print("a is greater")












