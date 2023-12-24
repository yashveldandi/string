#Strings: In python specifically, strings are a squence of a Unicode Characters

 
#1.Creating strings
s='hello'
s="hello"
#For  multiline strings
s="""hello"""
s='''hello'''
s=str('hello')
print(s)

#2.Accessing Substrings from a String

# Positive Indexing
s='hello world'
print(s[0])

#Negative indexing
s='hello world'
print(s[-1])

#Slicing
s='hello world'
print(s[0:5])
print(s[2:3])
print(s[2:])
print(s[:3])
print(s[:])

#step
#not print anything for that 1 number should be bigger for reverse
print(s[0:6:-1])

print(s[6:0:-1])

print(s[::-1])

#Editing and Deleting in string
s='hello world'

#Python string are immutable
# del s 
# print(s)

s='hello world'
# del s[-1:5:2]
# print(s)

#Operations on strings
"""Arithmetic Operations
Realtional Operations
Logical operators
Loops on Strings
Membership Operations"""

#arithmetic operations 
#concatination
print('delhi'+''+'mumbai')

print('delhi'*5)
print("*"*50)

#Relational Operators
a='delhi'=='mumbai'
print(a)

a='delhi'=='delhi'
print(a)

b='delhi'!='delhi'
print(b)

#Lexiographic(in dictionary mummbai come first after punr)
a='mumbai'>'pune'
print(a)

#Logical Operator
#ans-->world bec in and operator check bth condtions and print second cond

a='hello' and 'world'
print(a)

#in or condition see first one true then does not go to second conition
s='hello'or 'world'
print(s)

#not ! if true return false if false return true
a=not'hello'
print(a)

a=not ''
print(a)

# NOte : if emptyy string it take false value there than true

#Loops in strings
for i in 'hello':
    print(i)

#delhi mein jitne letters hai utnr bar pune print hoga
for i in 'delhi':
    print ('pune')    

#Membership operators
a='D' in 'Delhi'
print(a)

a='D' not in 'Delhi'
print(a)


#Common Functions
#There are 15 functions
#common function which are used in every datatype(list,str,tup,dict)
#len
#max
#min
#sorted

print(len('hello world'))
#it will print output acc to askey value
print(max("hello world"))
#min output is space as per askey space is smaller
print(min('hello world'))
# sorted always return output in list ascending order
print(sorted('hello world'))
#want output in descinding order
print(sorted('hello world',reverse=True))


#Functions which are only specific to string
#Captitalize/Title/Upper/Lower/Swapcase

#Capitalize -- It will capital 1 letter
s='hello world'
print(s.capitalize())

#title will capital both letters in sentence 
print(s.title())

#upper () it will convert all character in upper
print(s.upper())
s='Hello'
print(s.lower())
#Swapcase will convert cap char to small and small to cap
a='HeLo WoRld'
print(a.swapcase())


#Count/Find/Index

#count it will count the char how much time present in the sentence
print('my name is yash'.count(i))

#find
'''it will find the sentence index number where is present 
if the sentence is not present then retuen -1 means not present in senc'''

print('my name is yash'.find('is'))
# x is not present show -1
print('my name is yash'.find("x"))

#index
"""it is same as find if senc not present then throw error 
(in find it retuens -1)"""

print("my name is yash".index("is"))

# index if senc not present throw error
#print("my name is yash".index("x"))

#endswith/startswith

#endswith 
#sencentence endswith sh show true
print("my name is yash".endswith("sh"))

#flase bec endwith sh 
print("my name is yash".endswith("x"))

#Startwith
print("my name is yash".startswith("my"))

#Format(order matter)
name='yash'
gender='male'

print('Hi my name is {} and I am a {}'.format(name,gender))
print('Hi my name is {1} and I am a {0}'.format(name,gender))

#isalnum/isaplha/isdigit/isidentifier

#isalnum (means aplha numberic (alphabhet +numeric))
print('yash123'.isalnum())
#percent is not alphanumeric show false
print('yash123%'.isalnum())

#isalpha(work with only alphabet either give false)
print('yash'.isalpha())
#isaplha (num then false)
print('yash123'.isalpha())

#isdigit(only digit)
print('123'.isdigit())

#isdigit(only digit--add char then false)
print('123ys'.isdigit())

#isidentifer(means to set identifer the variable doesnot start with digit,specal symbol)
print('1name'.isidentifier())#-->false
print('name_1'.isidentifier())#--->True
print('first-name'.isidentifier())#-->Flase

#Split /Join(split the sentence in python list)
print('hi my name is yash'.split())#split sen in list
#split remove i and split the sentence
print('hi my name is yash'.split(i))

#Join (Reverse of split join the words and make sentence)
a=('my','name','is ','yash')
x=' '.join(a)
print(x)
print(' '.join(['my','name','is','yash']))

#Replace
print('my name is yash'.replace('yash','vasu'))

#if the sent is not there then it will send the original string
print('my name is yash'.replace('vasu','vasu'))

#STRIP("remove spaces")

print('yash      ' .strip())
print('yash      ' .strip())