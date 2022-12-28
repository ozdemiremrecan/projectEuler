def pisagor(a,b,c):
    return (a**2+b**2==c**2)
for i in range(500):
    for j in range(500):
        for k in range(500):
            if(i+j+k==1000):
                if(pisagor(i,j,k)):
                    print(i*j*k)
                else:
                    pass
            else:
                pass
