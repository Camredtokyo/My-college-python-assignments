#Dictinaries
d={'Math' : 98, 'English' : 97, 'Sci' : 95}
len(d)
print(len(d))
print(d)

#orddict
d['Math']
print(d['Math'])

d={'Math' : 98, 'English' : 97, 'Sci' : 95 ,'Math' : 100}
print(d)
#we can change the value of dictinary
d.keys()

d={'Math' : 98, 'English' : 97, 'Sci' : 95}
print(d.keys())
print(d.values())
print(d.items())

d={'Math' : 98, 'English' : 97, 'Sci' : 95 , 'Art' : 95}
d1={v:k for k,v in d.items()}
print(d)
print(d1)
print(d.pop('Art'))
print(d.popitem())
print(max(d))
print(min(d))
print(sum(d1))
del d
print(d)

