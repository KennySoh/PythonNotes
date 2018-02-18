def letter_grade(mark):
    if mark>100 or mark<0:
        return "None"
    elif mark>=90:
        return "A"    
    elif mark>=80:
        return "B"
    elif mark>=70:
        return "C"
    elif mark>=60:
        return "D"
    else:
        return "E"
        
print letter_grade (102)
print letter_grade (100)
print letter_grade (83)
