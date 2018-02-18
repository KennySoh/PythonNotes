

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
"""  
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
print ans"""
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