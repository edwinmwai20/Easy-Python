cost= [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]


def Stey(n):
    
    if(n in cost):
        n= n+2
    return (f"You are in step {n}")


print(Stey(8))

    