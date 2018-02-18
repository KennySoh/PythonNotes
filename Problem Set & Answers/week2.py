"""pcdit framework 
problem statement,test cases,
 design algorithm, implementation, testing"""


print ("\n Qns 1\n")
def fahrenheit_to_celsius(F):
    C=(F-32)*(5.0/9) #change to celsius
    return C
    
print fahrenheit_to_celsius(500)
print fahrenheit_to_celsius (32)
print fahrenheit_to_celsius (-40)

print ("\n Qns 2\n")
def position_velocity(v_0,t):
    g=9.81
    y_t=v_0*t-(1.0/2)*(g*t**2)
    y_diff_t=v_0-g*t
    y_t=round(y_t,2)
    y_diff_t=round(y_diff_t,2)
    return y_t,y_diff_t
    
print position_velocity (5.0 , 10.0)
print position_velocity (5.0 , 0.0)
print position_velocity (0.0 , 5.0)

print ("\n Qns 3\n")
def minutes_to_years_days(minutes):
    years=((minutes/60.0)/24.0)//365.0
    days=((minutes/60.0)/24.0)%365
    return int(years),int(days)
print minutes_to_years_days (1000000000)
print minutes_to_years_days (2000000000)

minutes_1=int(raw_input("Enter the number of minutes: "))
(x,y)=minutes_to_years_days (minutes_1)
print ("\n"+str(minutes_1)+" minutes is approximately "+str(x)+" years and "+str(y) +" days.")




print ("\n Qns 4\n")

from math import sqrt

class Coordinate:
    x = 0
    y = 0

def area_of_triangle(p1,p2,p3):
    s_1=sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
    s_2=sqrt((p1.x-p3.x)**2+(p1.y-p3.y)**2)
    s_3=sqrt((p3.x-p2.x)**2+(p3.y-p2.y)**2)
    s=(s_1+s_2+s_3)/2
    area=sqrt(s*(s-s_1)*(s-s_2)*(s-s_3))
    return area
    
print " Test Case 1"
p1= Coordinate ()
p1.x =1.5
p1.y= -3.4
p2= Coordinate ()
p2.x =4.6
p2.y=5
p3= Coordinate ()
p3.x =9.5
p3.y= -3.4
ans= area_of_triangle(p1 ,p2 ,p3)
print ans
print " Test Case 2"
p1= Coordinate ()
p1.x =2.0
p1.y= -3.4
p2= Coordinate ()
p2.x =4.6
p2.y=5
p3= Coordinate ()
p3.x =9.5
p3.y= -1.4
ans= area_of_triangle (p1 ,p2 ,p3)
print ans
print " Test Case 3"
p1= Coordinate ()
p1.x =1.5
p1.y =3.4
p2= Coordinate ()
p2.x =4.6
p2.y=5
p3= Coordinate ()
p3.x= -1.5
p3.y =3.4
ans= area_of_triangle (p1 ,p2 ,p3)
print ans
print " Test Case 4"
p1= Coordinate ()
p1.x= -1.5
p1.y =3.4
p2= Coordinate ()
p2.x =4.6
p2.y=5
p3= Coordinate ()
p3.x =4.3
p3.y= -3.4
ans= area_of_triangle (p1 ,p2 ,p3)
print ans

p1= Coordinate ()
p1.x=input("Enter x coordinate of the first point of a triangle: ")
p1.y=input("Enter y coordinate of the first point of a triangle: ")
p2= Coordinate ()
p2.x=input("Enter x coordinate of the second point of a triangle: ")
p2.y=input("Enter y coordinate of the second point of a triangle: ")
p3= Coordinate ()
p3.x=input("Enter x coordinate of the third point of a triangle: ")
p3.y=input("Enter y coordinate of the third point of a triangle: ")
print ("\nThe area of the triangle is "+ str(area_of_triangle (p1 ,p2 ,p3)))
print ("\n Qns 5\n")
def compound_value_sixth_months(amt, rate):
    month_1=amt*(1+rate/12)
    month_2=(amt+month_1)*(1+rate/12)
    month_3=(amt+month_2)*(1+rate/12)
    month_4=(amt+month_3)*(1+rate/12)
    month_5=(amt+month_4)*(1+rate/12)
    month_6=(amt+month_5)*(1+rate/12)
    return month_6

print compound_value_sixth_months (100 ,0.05)
print compound_value_sixth_months (100 ,0.03)
print compound_value_sixth_months (200 ,0.05)
print compound_value_sixth_months (200 ,0.03)

amt_1=input("Enter the monthly saving amount: ")
rate_1=input("Enter annual interest rate: ")
value=compound_value_sixth_months(amt_1, rate_1)
print ("\nAfter the sixth month, the account value is "+str(round((value),2)))
 