def bubblesorting(a):
    n=len(a)
    for i in range(n):
        swapped=0
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swapped=1
                #print(a)
        print(a)
        if(swapped==0):
            break
a=[3,7,4,9,1,10,8]
bubblesorting(a)
print(a)