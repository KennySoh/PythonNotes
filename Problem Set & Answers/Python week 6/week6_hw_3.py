import string
UpperCase = string.ascii_uppercase

def get_base_counts2(dna):

    counts={'A':0,'C':0,'G':0,'T':0}
    for base in dna:
        if base!='A' and base!='T' and base!='G' and base!='C'and base!=base.upper():
            return 'The input DNA string is invalid'            
        elif base=='A' or base=='C' or base=='T' or base=='G':
                 counts[base] += 1
    return counts

dna='AAAGGIII'  
print get_base_counts2(dna)