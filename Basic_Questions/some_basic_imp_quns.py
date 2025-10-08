# factorial of a given number 
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)


# The Factor of the given number is prime or not 
n=5
fact=1
for i in range(1,n+1):
    fact*=i
for j in range(2,fact//2):
    if fact%j==0:
        print(fact,"is not  a prime number ")
        break
else:
    print(fact,"is a prime number ")