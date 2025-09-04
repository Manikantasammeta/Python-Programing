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
    
    
