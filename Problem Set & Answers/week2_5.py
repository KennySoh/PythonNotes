print ("\n Qns 5\n")
def compound_value_sixth_months(amt, rate):
    month_1=amt*(1+rate/12)
    month_2=(amt+month_1)*(1+rate/12)
    month_3=(amt+month_2)*(1+rate/12)
    month_4=(amt+month_3)*(1+rate/12)
    month_5=(amt+month_4)*(1+rate/12)
    month_6=(amt+month_5)*(1+rate/12)
    return month_6
"""
print compound_value_sixth_months (100 ,0.05)
print compound_value_sixth_months (100 ,0.03)
print compound_value_sixth_months (200 ,0.05)
print compound_value_sixth_months (200 ,0.03)
"""
amt_1=input("Enter the monthly saving amount: ")
rate_1=input("Enter annual interest rate: ")
value=compound_value_sixth_months(amt_1, rate_1)
print ("\nAfter the sixth month, the account value is "+str(round((value),2)))
 