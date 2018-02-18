
print ("\n Qns 3\n")
def minutes_to_years_days(minutes):
    years=((minutes/60.0)/24.0)//365.0
    days=((minutes/60.0)/24.0)%365
    return int(years),int(days)
"""
print minutes_to_years_days (1000000000)
print minutes_to_years_days (2000000000)
"""
minutes_1=int(raw_input("Enter the number of minutes: "))
x,y=minutes_to_years_days (minutes_1)
print ("\n"+str(minutes_1)+" minutes is approximately "+str(x)+" years and "+str(y) +" days.")


