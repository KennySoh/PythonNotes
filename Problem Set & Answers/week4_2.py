

def compound_value_months(monthly_saving,rates,n):
    monthly_rates=rates/12.0+1.0
    counter=1
    Total=0.0
    while (counter<=n):
        Total=(Total+monthly_saving)*monthly_rates
        counter=1+counter
    
    return round(Total,2)
    
ans= compound_value_months (100 ,0.05 ,6)
print ans
#608.81
ans= compound_value_months (100 ,0.03 ,7)
print ans
#707.04
ans= compound_value_months (200 ,0.05 ,8)
print ans
#1630.29
ans= compound_value_months (200 ,0.03 ,1)
print ans
#200.5