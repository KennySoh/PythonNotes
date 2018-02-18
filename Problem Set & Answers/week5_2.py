from fractions import Fraction
def leap_year(year):
# true if arguement year is leap year  mutiple of 4
    x=Fraction(year/4.0)
    if Fraction(x).denominator==1:
        x=Fraction(year/100.0)
        if Fraction(x).denominator==1:
            x=Fraction(year/400.0)
            if Fraction(x).denominator==1:
                return True
            else:
                return False
        else:
            return True
    else: 
        return False
        
def day_of_week_jan1(A):
#return the day of the week for jan 1 of the input arguement
#year must be between 1800 and 2099
#return value must be 0-6 (0-sun..... 6-sat)
    x=R(1+5*R((A-1),4)+4*R((A-1),100)+6*R((A-1),400),7)
    return x
def R(y,m):
    return y%m
def num_days_in_month(month_num,leap_year):
#month_num must be 1- 12 /  leap_year is true or false
#Returns the number of days in a given month
    if month_num in [1,3,5,7,8,10,12]:
        return 31
    if month_num==2:
        if leap_year==True:
            return 29
        else:
            return 28
    return 30
def construct_cal_month(month_num,first_day_of_month, num_days_in_month):
#return a formatted calendar month for display on the screen.
# month_num must be 1 -12 first day is 0- 6 sunday-0  sat-6
# retunn [month_name , week 1 ,week2 ,....]
    month=['invalid','January','February','March','April','May','June','July','August','September','October','November','December']
    results=[month[month_num]]
    s='   '*first_day_of_month
    for i in range (1,num_days_in_month+1):
        s=s+'%3d'%i
        if len(s)==7*3:
            results.append(s)
            s=''
        elif i==num_days_in_month:
            
            results.append(s)
        
    return results
def construct_cal_year(year):
    ls=[year]
    ly=leap_year(year)
    fd=day_of_week_jan1(year)
    
    for i in range(1,13):
         num=num_days_in_month(i,ly)
         ls.append(construct_cal_month(i,fd,num))
         fd=fd+num
         fd=fd%7
         #print fd
    return ls

def display_calendar(calendar_year,months):
    ls=construct_cal_year(calendar_year)
    s=""
    #print ls
    for i in range(0,len(ls)):
        
        if type(ls[i])==list:
            for j in range(0,len(ls[i])):
                #print ls[i][j]
                if j==1:
                   s=s+"  S  M  T  W  T  F  S"+"\n"
                
                s=s+ls[i][j]
                if j<len(ls[i])-1:
                    s=s+"\n"
        if i<len(ls)-1:
            if i==0:
                s=s
            else:
                s=s+"\n"+"\n"
    if months!=None:
        s=''
        #for i in range(0,len(ls)):
        i=months    
        if type(ls[i])==list:
            for j in range(0,len(ls[i])):
                    #print ls[i][j]
                if j==1:
                    s=s+"  S  M  T  W  T  F  S"+"\n"
                        
                s=s+ls[i][j]
                if j<len(ls[i])-1:
                    s=s+"\n"
        if i<len(ls)-1:
            if i==0:
                s=s
            else:
                s=s

        
    #print s
    return s  
print display_calendar(2000,3)