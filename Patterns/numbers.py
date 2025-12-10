n=7
for i in range(n):
    for j in range(n):
        if j==n//2 or i==n-1 or j==n//2-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#       *       
#     * *       
#   *   *
# *     *
#       *
#       *
# * * * * * * *







n=7
for i in range(n):
    for j in range(n):
        if i==0 or (j==n-1 and i<=n//2) or i==n//2 or (j==0 and i>=n//2) or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# * * * * * * * 
#             * 
#             * 
# * * * * * * * 
# *             
# *             
# * * * * * * * 

n=7
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1  or i==n//2  or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# * * * * * * * 
#             * 
#             * 
# * * * * * * * 
#             * 
#             * 
# * * * * * * *


n=7
for i in range(n):
    for j in range(n):
        if j==(n//2)+1 or i==(n//2)+1  or i+j==n//2+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
      
#         *     
#       * *     
#     *   *     
#   *     *     
# * * * * * * * 
#         *     
#         *     


n=7
for i in range(n):
    for j in range(n):
        if i==0 or (j==0 and i<=n//2) or i==n//2 or (j==n-1 and i>n//2) or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# * * * * * * * 
# *             
# *             
# * * * * * * * 
#             * 
#             * 
# * * * * * * * 

n=7
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==n//2 or (j==n-1 and i>n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# * * * * * * * 
# *             
# *             
# * * * * * * * 
# *           * 
# *           * 
# * * * * * * * 


n=7
for i in range(n):
    for j in range(n):
        if i==0  or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# * * * * * * * 
#           *   
#         *     
#       *       
#     *         
#   *           
# *   











n=7
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# * * * * * * * 
# *           * 
# *           * 
# * * * * * * * 
# *           * 
# *           * 
# * * * * * * *           

n=7
for i in range(n):
    for j in range(n):
        if i==0 or (j==0 and i<=n//2) or j==n-1 or i==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# * * * * * * * 
# *           * 
# *           * 
# * * * * * * * 
#             * 
#             * 
# * * * * * * * 