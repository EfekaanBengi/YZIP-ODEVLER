def rec_Fac(x):
    if x == 0 or x == 1:
        return 1
    return rec_Fac(x - 1) * x 


def iter_Fac(x):
    total = 1
    for i in range(1,x+1):
        total = total*i
    
    return total

print(rec_Fac(6))
print(iter_Fac(6))