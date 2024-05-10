d={'Alex':['subj1','subj2','subj3'],'David':['subj2']}
# c=0
# for x in d:
#     if isinstance(d[x],list):
#         c=c+1
# print(c)

i=0
while i < d:
    



c=0
for i in d:
    if d[i]:
        c=c+len(d[i])
print(c)        

