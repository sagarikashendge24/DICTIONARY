j="MISSISSIPPII"
i=0
a=b=c=d=0
e={}
while i <len(j):
    if j[i]=="M":
        a=a+1
    if j[i]=="I":
        b=b+1
    if j[i]=="S":
        c=c+1
    if j[i]=="P":
        d=d+1
    i=i+1
l=("M:",a,"I:",b,"S:",c,"P:",d)
yprint (l)


# d=dict()
# for c in j:
#     if c not in d:
#         d[c]=1
#     else:
#         d[c]=d[c]+1
# print(d)      

