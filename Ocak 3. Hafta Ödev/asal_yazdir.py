def asal_Mi(sayi):

    if sayi <= 1:   
        return False


    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    
    return True
            


for i in range(101):
    if asal_Mi(i):
        print(i)














































