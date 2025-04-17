s1="madam"
s2="mahi"
print(*[s1[i] for i in range(len(s2)) if s1[i]==s2[i] ])

print(set(s1).intersection(set(s2)))

