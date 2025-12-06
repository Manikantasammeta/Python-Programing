
#                ALL THE PYTHON CODE ARE COMMENTED. IF YOU WANT TO RUN AND EXECUTE THE CODE,JUST UNCOMMENT THE CODE. 
#                THE RESPECTIVE OUTPUT WILL BE DISPLAYED AT THE BOTTOM OF THE CODE. CHECK IT ONCE.

# L=["rama","raju","raghu","mani","sita"]
# print([ i[0].upper()+":"+i for i in L])

#Output ['R:rama', 'R:raju', 'R:raghu', 'M:mani', 'S:sita']   #convertintg the list into list

input_list=[[1,2],[3,4],[5,6],[7,8]]
list_comp=[j  for i in input_list for j in i]
print(list_comp)  #[1, 2, 3, 4, 5, 6, 7, 8]





it=iter(input_list)

print(dir(it))
print(len(input_list))