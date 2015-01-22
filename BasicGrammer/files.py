#coding:utf-8
__author__ = 'oliver'

f = open("files/test.txt","r")
#只读到第一个字母I
#print(f.read(1))
#从I 后面往下,不包含第一个字母
#print(f.read())
#读到的是空
print(f.readline())
'''
for i in f:
    print(i)
'''
myList = []
for line in f:
    myList.append(line)
print(myList)

f.close()

#覆盖模式
f = open("files/test2.txt","w")
f.write("I'm the King of the world!\n")
f.close()


f = open('files/test2.txt',"a")
f.write("I'm the Queen of the world!\n")
f.close()

