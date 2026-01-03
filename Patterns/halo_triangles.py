'''
n=5 
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
output:    
*         
* *       
*   *     
*     *   
* * * * * 

n=5
for i in range(n):
    for j in range(n):
        if i==n-1 or j==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
output:
        * 
      * * 
    *   * 
  *     * 
* * * * * 


n=5 
for i in range(n):
    for j in range(n):
        if i==j or i==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

output:
* * * * * 
  *     * 
    *   * 
      * * 
        * 


n=5
for i in range(n):
    for j in range(n):
        if i==0 or i+j==n-1 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
output
* * * * * 
*     *   
*   *     
* *       
* 


n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
output
* * * * * 
*       * 
*       * 
*       * 
* * * * * 


n=5
for i in range(n):
    for j in range((2*n)-1):
        if i+j==n-1 or i==n-1 or j-i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
output
        *         
      *   *       
    *       *     
  *           *   
* * * * * * * * * 


n=6
for i in range(n):
    for j in range((2*n)-1):
        if i==0 or i==j  or i+j==(2*n)-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
output:   
* * * * * * * * * * * 
  *               *   
    *           *     
      *       *       
        *   *         
          *  


n=5
for i in range((2*n)-1):
    for j in range(n):
        if j==0 or i==j or i+j==2*n-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
output 
*         
* *       
*   *     
*     *   
*       * 
*     *   
*   *     
* *       
*  


n=5
for i in range((2*n)-1):
    for j in range(n):
        if j==n-1 or i+j==n-1 or i-j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

        * 
      * * 
    *   * 
  *     * 
*       * 
  *     * 
    *   * 
      * * 
        * 

n=13
for i in range(n):
    for j in range(n):
        if i==j or j+i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
output:



n=13
for i in range(n):
    for j in range(n):
        if i==j or j+i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
output
*                       * 
* *                   * * 
*   *               *   * 
*     *           *     * 
*       *       *       * 
*         *   *         * 
*           *           * 
*         *   *         * 
*       *       *       * 
*     *           *     * 
*   *               *   * 
* *                   * * 
*                       * 


n=13
for i in range(n):
    for j in range(n):
        if i==j or j+i==n-1 or j==0 or j==n-1 or i==0 or j==0 or i==n-1 or i==n//2 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
output

* * * * * * * * * * * * * 
* *         *         * * 
*   *       *       *   * 
*     *     *     *     * 
*       *   *   *       * 
*         * * *         * 
* * * * * * * * * * * * * 
*         * * *         * 
*       *   *   *       * 
*     *     *     *     * 
*   *       *       *   * 
* *         *         * * 
* * * * * * * * * * * * * 

'''