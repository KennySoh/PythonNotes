def interlock(word1, word2, word3):
    word_combined=[]
    if len(word1)!=len(word2):
        return False
    if len(word1)+len(word2)!=len(word3):
        return False
    else:
        x_1=0
        for x in range(0,len(word1)):
            word_combined.append(word1[x])
            word_combined.append(word2[x])
        word_combined= ''.join(word_combined)
    if word_combined!=word3:
        return False
    return True
        
print interlock("shoe", "cold", "schooled")