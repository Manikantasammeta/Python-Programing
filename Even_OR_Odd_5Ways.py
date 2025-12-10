# Normal Method 
n=5
if n%2==0:
    print("Even")
else:
    print("Odd")
    
# without using "==" operator
if n%2:
    print("Odd")
else:
    print("Even")
 
 
  
  
    
# without using " % " operator
if (n//2)*n==n:
    print("Even")
else:
    print("Odd")
 
    
# with using " % " and " == " operator
if n//2*2 is n:
    print("Even")
else:
    print("Odd")
    
# with using " & " operator   
if n&1==0:
    print("Even")
else:
    print("Odd")
    
# with using " | " operator   
if n|1==n:
    print("Odd")
else:
    print("Even")
    
# with using " ^ " operator   
if n^1==n:
    print("Even")
else:
    print("Odd")
    
# with using list   
l=['Even','Odd']
print(l[n%2])

    
