def extract_values(values):
    values=values.split(" ")
    results=(int(values[0]),int(values[1]))

    return results
def calc_ratios(values):
    x=float(values[0])
    y=float(values[1])
    if values[1]==0:
        return None
    z=x/y
    return z
def get_data():
    input_var=raw_input("Enter integer pair (hit Enter to quit) :")
    return input_var
print calc_ratios(extract_values(get_data()))