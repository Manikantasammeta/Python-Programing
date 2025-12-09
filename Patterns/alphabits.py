n=5
for i in range(n+1):
    for j in range(2*n+1):
        if i+j==n or (i==(n//2)+1 and n//2<=j<=(n//2)+n+1) or j-i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
 
 
 
 
 
 
    
    
#           *           
#         *   *         
#       *       *       
#     * * * * * * *     
#   *               *   
# *                   * 
    
