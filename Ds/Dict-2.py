# import random as rm
# class my_marks:
#     # names=["mani","mahesh","abhinav","abhi","sadha","reddy","pinky","raju","rani","rowdy","roja","sai","siva","gopi","shiva"]
#     # math=[100, 85, 67, 95, 73, 96, 86, 78, 93, 98, 92, 68, 99, 83, 83]
#     # phy=[86, 80, 89, 96, 73, 89, 69, 87, 89, 66, 97, 73, 65, 79, 89]
#     # eng=[88, 77, 98, 88, 71, 71, 96, 69, 73, 83, 77, 95, 96, 66, 67]
#     # che=[80, 98, 88, 92, 88, 74, 66, 82, 73, 91, 81, 78, 75, 88, 78]
#     global mydic
#     mydic={'mani': {'math': 100, 'phy': 86, 'eng': 88, 'che': 80, 'total': 354},
#            'mahesh': {'math': 85, 'phy': 80, 'eng': 77, 'che': 98, 'total': 340}, 
#            'abhinav': {'math': 67, 'phy': 89, 'eng': 98, 'che': 88, 'total': 342}, 
#            'abhi': {'math': 95, 'phy': 96, 'eng': 88, 'che': 92, 'total': 371}, 
#            'sadha': {'math': 73, 'phy': 73, 'eng': 71, 'che': 88, 'total': 305}, 
#            'reddy': {'math': 96, 'phy': 89, 'eng': 71, 'che': 74, 'total': 330}, 
#            'pinky': {'math': 86, 'phy': 69, 'eng': 96, 'che': 66, 'total': 317}, 
#            'raju': {'math': 78, 'phy': 87, 'eng': 69, 'che': 82, 'total': 316}, 
#            'rani': {'math': 93, 'phy': 89, 'eng': 73, 'che': 73, 'total': 328}, 
#            'rowdy': {'math': 98, 'phy': 66, 'eng': 83, 'che': 91, 'total': 338}, 
#            'roja': {'math': 92, 'phy': 97, 'eng': 77, 'che': 81, 'total': 347}, 
#            'sai': {'math': 68, 'phy': 73, 'eng': 95, 'che': 78, 'total': 314}, 
#            'siva': {'math': 99, 'phy': 65, 'eng': 96, 'che': 75, 'total': 335}, 
#            'gopi': {'math': 83, 'phy': 79, 'eng': 66, 'che': 88, 'total': 316}, 
#            'shiva': {'math': 83, 'phy': 89, 'eng': 67, 'che': 78, 'total': 317}}










#     # def list_of_marks(self):

#     #     self.d=dict()
#     #     for i in range(len(self.names)):
#     #         n=self.names[i]
#     #         for j in range(4):
#     #             d1={}
#     #             d1.update({"math":self.math[i]})
#     #             d1.update({"phy":self.phy[i]})
#     #             d1.update({"eng":self.eng[i]})
#     #             d1.update({"che":self.che[i]})
#     #             d1.update({"total":int(self.math[i]+self.phy[i]+self.eng[i]+self.che[i])})
#     #         self.d.update({n:d1})
#     #     return self.d
    
    
    
    
#     def display(self):
#         print("-"*85)
#         print(f"""Name          MATH            PHT             ENG             CHE             TOTAL""")
#         print("-"*85)
#         for i in mydic:
#             print(f"""{i}""")  

# l=my_marks()
# l.display()


# mydic={     'mani': {'math': 100, 'phy': 86, 'eng': 88, 'che': 80, 'total': 354},
#            'mahesh': {'math': 85, 'phy': 80, 'eng': 77, 'che': 98, 'total': 340}, 
#            'abhinav': {'math': 67, 'phy': 89, 'eng': 98, 'che': 88, 'total': 342}, 
#            'abhi': {'math': 95, 'phy': 96, 'eng': 88, 'che': 92, 'total': 371}, 
#            'sadha': {'math': 73, 'phy': 73, 'eng': 71, 'che': 88, 'total': 305}, 
#            'reddy': {'math': 96, 'phy': 89, 'eng': 71, 'che': 74, 'total': 330}, 
#            'pinky': {'math': 86, 'phy': 69, 'eng': 96, 'che': 66, 'total': 317}, 
#            'raju': {'math': 78, 'phy': 87, 'eng': 69, 'che': 82, 'total': 316}, 
#            'rani': {'math': 93, 'phy': 89, 'eng': 73, 'che': 73, 'total': 328}, 
#            'rowdy': {'math': 98, 'phy': 66, 'eng': 83, 'che': 91, 'total': 338}, 
#            'roja': {'math': 92, 'phy': 97, 'eng': 77, 'che': 81, 'total': 347}, 
#            'sai': {'math': 68, 'phy': 73, 'eng': 95, 'che': 78, 'total': 314}, 
#            'siva': {'math': 99, 'phy': 65, 'eng': 96, 'che': 75, 'total': 335}, 
#            'gopi': {'math': 83, 'phy': 79, 'eng': 66, 'che': 88, 'total': 316}, 
#            'shiva': {'math': 83, 'phy': 89, 'eng': 67, 'che': 78, 'total': 317}}



# print("-"*105)
# print(f"""NAME              MATH                PHY                 eng                 che                 total""")
# print("-"*105)
# for i in mydic:
#     print(i)
#     if
            


# D={'RAJU': {'Eng': 0, 'Phy': 90, 'Math': 46}, 
#  'PINKY': {'Phy': 45, 'Eng': 65, 'Math': 0}, 
#  'SITA': {'Math': 46, 'Eng': 50, 'Phy': 45}, 
#  'MAHESH': {'Eng': 0, 'Phy': 19, 'Math': 99}}

                # Difference between total marks of RAJU and SITA:
# Raju=0
# Sita=0
# for name, scrs in D.items():
#     for sub,mrk in scrs.items():
#         if name=='RAJU':
#             Raju=Raju+mrk
#         elif name=='SITA':
#             Sita=Sita+mrk
# print('Markes of Raju',Raju)
# print('Markes of Sita',Sita)
# print(abs(Raju-Sita)) 



                 #Fins the Students Names and Subjects who are get Zero in any subject
# Output={}       
# for name,scrs in D.items():
#     for sub,mrk in scrs.items():
#         if mrk==0:
#             Output[name]=sub
# print(Output)

# Output={'RAJU': 'Eng', 'PINKY': 'Math', 'MAHESH': 'Eng'}

                     #Find the Ranks of the Students according to their Marks 
                    
# names=list(D.keys())
# marks=[]
# output={}

# for name,scrs in D.items():
#     m=0
#     for sub,mrk in scrs.items():
#         m+=mrk
#     marks.append(m)
# old=marks.copy()
# marks.sort(reverse=True)
# for i in range(len(marks)):
#     idx=old.index(marks[i])
#     output[i+1]=names[idx]
# print(output)

# Output:{1: 'SITA', 2: 'RAJU', 3: 'MAHESH', 4: 'PINKY'}



                # Write a program to count how many times each word appears in a sentence.
# s="hello world hello python python python".split()
# output={}
# for i in s:
#     output[i]=s.count(i)
# print(output) {'hello': 2, 'world': 1, 'python': 3}

        # Find how many “n” present in the given range numbers 
        
# start=100
# end=130
# n=3
# output=0
# for i in range(start,end+1):
#     cnt=0
#     while i !=0:
#         ele=i%10
#         if ele==n:
#             cnt+=1
#         i=i//10
#     output+=cnt
        
# print(output)

        #Merge two dictionaries by adding the values of common keys.




        #Group a list of words into anagrams using a dictionary.

# l=["bat", "tab", "cat", "act", "tac"]
# d={}
# for i in l:
#     key="".join(sorted(i))
#     if key in d:
#         d[key].append(i)
#     else:
#         d[key]=[i]
# print(d){'abt': ['bat', 'tab'], 'act': ['cat', 'act', 'tac']}

            # Given a dictionary where values can repeat, return a reverse dictionary where each value maps to a list of keys.
# d={'a': 1, 'b': 2, 'c': 1}
# d1={}
# for key,value in d.items():
#     if value in d1:
#         d1[value].append(key)
#     else:
#         d1[value]=[key]
# print(d1)#{1: ['a', 'c'], 2: ['b']}


                #Convert a dictionary to a list of tuples and sort by keys in descending order.
# Input={'x': 5, 'a': 10, 'm': 3}
# out=[]
# for key,value in Input.items():
#     out.append((key,value))
# print(out)   #[('x', 5), ('a', 10), ('m', 3)]
 
 
 
            #Return a dictionary with the count of vowels and consonants in a string.
# s="hello world"
# out={}
# vowels=0
# consonants=0
# for i in s:
    
#     if i in "aeiou":
#         vowels+=1
#     elif i in "bcdfghjklmnpqrstvwxyz":
#         consonants+=1
# out["vowels"]=vowels
# out["consonants"]=consonants
# print(out) #{'vowels': 3, 'consonants': 7}


            # Map each character in a string to a list of its positions (indices).
# s="banana"
# out = {}
# for i in range(len(s)):
#     if s[i] in out:
#         out[s[i]].append(i)
#     else:
#         out[s[i]] = [i]
# print(out)#{'b': [0], 'a': [1, 3, 5], 'n': [2, 4]}


            # Map each word to a set of its unique characters.
# s="hello world"
# out={}
# for i in s.split():
#     out[i]=set(i)
# print(out)# {'hello': {'e', 'l', 'h', 'o'}, 'world': {'o', 'd', 'w', 'l', 'r'}}