n=5
for i in range(n):
    for j in range(n):
        if j==n//2 or i==n-1 or j==n//2-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()