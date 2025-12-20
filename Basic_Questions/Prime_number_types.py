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

def check_prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
    
    
# prime numbers between range 

starting_range =2   # or else use can take any user input here like  int(input("Enter the starting range"))
ending_range=199    # or else use can take any user input here like  int(input("Enter the ending range"))

for i in range(starting_range,ending_range+1):
    if check_prime(i):
        print(i,"is a prime number")
    else:
        print(i,"is not a Prime number")
        

# with out using functions 

starting_range =2
ending_range=199

for i in range(starting_range,ending_range):
    for j in range(2,(i//2)+1):
        if i%j==0:
            break
    else:
        print(i,"is a Prime number")
    
    
    
# Nth Prime number  that meance n=2 we need to find the 2nd prime number that is 3
n=3 # output=5 , that is prime numbers start from 2, 3, 5, 7, ., ., .... so 2nd prime number is 3
p_cnt=0
i=2
while True :
    if check_prime(i):
        p_cnt+=1
    if p_cnt ==n:
        print(n,"th prime number is ",i)
        break
    i+=1
    
    
