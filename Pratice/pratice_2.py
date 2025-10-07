import math, random as rm

def sud_str(string, out=None):
    if out is None:
        out = []
    if len(out) <= math.factorial(len(string)):
        ln = rm.randint(1, len(string))
        s = []
        for i in range(ln):
            char = string[rm.randint(0, len(string) - 1)]
            if char not in s:
                s.append(char)
        substr = "".join(s)
        if substr not in out:
            out.append(substr)
        sud_str(string, out)



    return out

print(sud_str("123"))



# Prime Factors of a given number 
n=10 
i=1
while i<=n:
    if n%i==0:
        for j in range(2,i//2):
            if i%j==0:
                break
        else:
            print(i)
    i+=1
