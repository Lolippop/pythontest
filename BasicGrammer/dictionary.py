#coding:utf-8
#字典使用方式
mydictionary = {"name" : "wuchenqiu", "value" : 10}
print(mydictionary["name"])
for i in mydictionary:
	print(mydictionary[i])
#字典中嵌套tuple dict list str
mySecDic = {"name" : "wuchenqiu","myarray" : [1,2,3,4,5], "mydic" : mydictionary,"mytuple" : (1,2,3,4,5)}
print(mySecDic["myarray"])
print(mySecDic["mydic"])
for j in mySecDic:
    if(list == type(mySecDic[j])):
        print(mySecDic[j])
    elif(tuple == type(mySecDic[j])):
        print(mySecDic[j])
