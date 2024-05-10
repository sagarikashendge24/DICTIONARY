# a={}
# b=int(input("How much input????"))
# for i in range(b):
#     j=input("Enter the key")
#     s=input("Enter the values")
#     a.update({j:s})
# print(a)   


i=0
# a=[]
dic1={}
while i<3:
    user=input("Enter the key")
    num=int(input("Enter the values"))
    i=i+1
    d={user : num }
    dic1.update(d)
    # a.append(d)
print(dic1)    
# print(a)