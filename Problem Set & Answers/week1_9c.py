Name= raw_input('Pls Enter Your Name: ')
while True:
    ID=raw_input("Pls Enter Your ID: ")
    try:ID=int(ID)
    except: print "Please enter a number."
    else :  break
Q_M,P_M,FP_M=raw_input("Pls enter Your Marks for Quiz,Project,Final Paper (eg: 100 100 100) : ").split()

Average_M=(float(Q_M)+float(P_M)+float(FP_M))/3.0 #average marks
if Average_M>=90:
    Grade= "A"
elif Average_M>=80:
    Grade= "B"
elif Average_M>=70:
    Grade= "C"
elif Average_M>=60:
    Grade= "D" 
else:
    Grade= "F"
print ("\nName: "+Name+ ", ID: "+ str(ID) +", Average Mark: "+ str(Average_M)+", Grade: "+Grade)

