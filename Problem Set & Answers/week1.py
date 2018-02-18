# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:45:24 2017

@author: Kenny
"""

print("Qns 1\n")
print type("This is the first Week!")
print "This is the first Week!"
print type(24)
print 24
print type(2.4)
print 2.4
print type("24")
print "24"
print type('2.4')
print type("""2.4""")
print type('''2.4''')
print 10300
print 10,300
print 10.300
print type(10.300)

print "\n Qns 2 \n"

print int(1.1)
print int(9.81)
print int(-9.81)
#print int("9.81") 
print("Error")
# print int("9.81m/s2")
print("Error")
print float("9.81")
print str(9.81)
print type(str(9.81))
print str(int(9.81))
print type(str(int(9.81)))

print "\n Qns 3 \n"
#message = " What 's up , Doc?"
#n = 17
#pi = 3.14159
#pi = 3.14
#print message
#print n
#print pi

print "Not defined"
print "Not defined"
print "3.14159"
print "3.14"
print "String"
print "INT"
print "float"
#Line 3 means before line 3 havent read line 3

print "\n Qns 4 \n"

#23days
#days23
#day 23
#mymoney2=1
#mymoney$
myclass=1
#class=1
#my_grade
#my_grade_is_B+=1

"""Variable names must start with letters or an underscore
Variables are case sensitive
The rest of the variable can consist of letters,numbers and underscores
readable and case sensitive"""

print "\n Qns 5 \n"
"""
1 class Coordinate ( object ):
2 x = 3.2
3 y =-1.5
4 p1 = Coordinate ()
5 p2 = Coordinate ()
6 p2.x = 0.3
7 p2.y = 1.0
"""

class Coordinate ( object ):
    x = 3.2
    y =-1.5
p1 = Coordinate ()
p2 = Coordinate ()
p2.x = 0.3
p2.y = 1.0

print type(p1)
print type(p2)
print type(Coordinate)
print p1.x, p1.y
print p2.x, p2.y

print "\n Qns 6 \n"

print 5 + 3
print 5 - 3
print 5 * 3
print 5 ** 3
print 5 / 3
print 5 // 3
print 5 / 3.0
print 5.0 / 3
print 5 % 3

""" Operators
**: exponentiation
^: exclusive-or (bitwise)
%: modulus
//: divide with integral result (discard remainder)
"""
print "\n Qns 7 \n"
print 17-3*7/4+1
print 2**2**4*3

print "\n Qns 8 \n"

x = 3
print x,
x = x + 2
print x
print "\n"
x = 3
print x,
x -= 2
print x
print "\n"
x = 3
print x,
x *= 2
print x

print "\n Qns 9 \n"

"""Strings
a="hello "
b="world"
c=a+b
print c
print len(c)
"""

"""Class is object oriented, methods stores properties
class Employee:
pass

emp_1 = Employee ()
emp_2 = Employee ()

"""
"""
FLowCharts outlines the program using Start End input output sum(programinternal) conditions
Functions takes input and send output eg.len()
 """