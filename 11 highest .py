d={'a':50, 'b':58,'c':56,'d':40,'e':100,'f':20}
n=[]
l=[]
for i in d.values():
    n.append(i)        
i=0
c=n[i]
while i<len(n):
    j=n[i]
    if j>c:
        c=j
    i=i+1
n.remove(c)
k=0
s=n[1]
while k<len(n):
    m=n[k]
    if m>s:
        s=m
    k=k+1
n.remove(s)
k=0
p=n[1]
while k<len(n):
    m=n[k]
    if m>p:
        p=m
    k=k+1
l.append([c,s,p])
print(l)



# k=[]
# for x in d.values():
#     k.append(x)
# i=0
# while i<len(k):
#     j=0
#     while j<len(k)-1:
#         if k[j]>k[j+1]:
#             k[j],k[j+1]=k[j+1],k[j]
#         j=j+1
#     i=i+1
# # print(k)
# a=k[-3:]
# print(a)        
