#  1. Bubble Sort	
l=[2,5,7,1,9,6,3,8,4,]

for i in range(1,len(l)):
    for j in range(0,len(l)):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l) # [1, 2, 3, 4, 5, 6, 7, 8, 9]






# 2.Selection Sort
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3.Insertion Sort
for i in range(1,len(l)):
    for j in range(i-1,0,-1):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l) #[1, 2, 3, 4, 5, 6, 7, 8, 9]