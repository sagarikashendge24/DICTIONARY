d=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
c={}
for i in d:
    c.update(i)
a=[]    
for i in c.values():
    if i not in a:
        a.append(i)
print(a)
