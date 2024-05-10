list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
# c={}
# for n in range (len(list1)):
#   c[list1[n]]=list2[n]
# print(c)  



i=0
my_dic1={}
length=len(list1)
while i<length:
    new_dic={list1[i]:list2[i]}
    my_dic1.update(new_dic)
    i=i+1
print(my_dic1)    