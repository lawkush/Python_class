n1=11
n2=45
for i in range(n1,n2+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        print("Prime number in an interval",i)
