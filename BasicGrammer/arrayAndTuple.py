myarray = [3,2,1,4,5]
myarray.append("23")
myarray.sort()
for i in myarray:
	print(type(i))
	print(i)
mytuple = (3,2,1,4,5)
#mytuple.sort();  --this is wrong
#mytuple.append("ab")  --this is wrong too tuple object has no attribute 'sort and append'
#the length of tuple can not be changed
for i in mytuple:
	print(i)

mylist = list(mytuple)
mylist.append("2345")
for i in mylist:
	print(i)
