#check the Given number is prime number or not

# -By using While loop .

n=5
d=2
cnt=0
while d<=n:
    if n%d==0:
        cnt=cnt+1
    d+=1
if cnt==2:
    print(n,"is Prime number")
else:
    print(n,"not a prime number")
    
    
# - By using for loop 

n=5 
for i in range(2,n):
    if n%i==0:
        print(n,"not a Prime number")
        break
else:
    print(n,"is a Prime number ")
    

# By useing functions 

def check_prime_(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True

    
    