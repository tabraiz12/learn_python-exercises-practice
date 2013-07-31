def createGenerator():
    mylist = range(3)
    for i in mylist:
       yield i*i

mygenerator = createGenerator()
mygenerator1 = createGenerator()
print(mygenerator)
for i in mygenerator:
    print(i)

print(mygenerator1)
for i in mygenerator1:
    print(i)