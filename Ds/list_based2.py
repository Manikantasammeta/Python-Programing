
#                ALL THE PYTHON CODE ARE COMMENTED. IF YOU WANT TO RUN AND EXECUTE THE CODE,JUST UNCOMMENT THE CODE. 
#                THE RESPECTIVE OUTPUT WILL BE DISPLAYED AT THE BOTTOM OF THE CODE. CHECK IT ONCE.

# L=["rama","raju","raghu","mani","sita"]
# print([ i[0].upper()+":"+i for i in L])

#Output ['R:rama', 'R:raju', 'R:raghu', 'M:mani', 'S:sita']   #convertintg the list into list

input_list=[[1,2],[3,4],[5,6],[7,8]]
list_comp=[j  for i in input_list for j in i]
print(list_comp)  #[1, 2, 3, 4, 5, 6, 7, 8]



s="abc13ef5"
s1=""
status=False
num=""
strr=""
for i in s:
    if i.isdigit():
        num+=i
        status=True
    elif i.isalpha():
        if status==True:
            s1=strr*int(num)
            strr=""
            num=""
            status=False
        strr+=i
s1+=strr*int(num)    
print(s1)