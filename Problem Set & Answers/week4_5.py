def get_details(name,keysearch,ls):
    #exDict={andrew:[mobile,office,email],bob:[mobile,office,email]}
    counter=0
    while counter<len(ls):
        if ls[counter]["name"]==name:
            return ls[counter][keysearch]
        counter+=1
    return None

phonebook =[{"name":"Andrew", "mobile_phone":9477865 , 'office_phone':6612345 , 'email':' andrew@sutd . edu.sg '},{'name':'Bobby','mobile_phone':8123498 , 'office_phone':6654321 , 'email':'bobby@sutd .edu.sg '}]
print get_details ("Andrew", "mobile_phone", phonebook )
#9477865
print get_details ("Andrew", "email", phonebook )
#andrew@sutd .edu.sg
print get_details ("Bobby", "office_phone", phonebook )
#6654321
print get_details ("Chokey", 'office_phone', phonebook )
#None