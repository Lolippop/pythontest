#coding:utf-8
__author__ = 'oliver'
#自定义异常
var1 = '1'
try:
    var1 = var1 + 1
except:
    print(var1," is not a number")
  #  var1 = var1 + 'str'
    var1 = int(var1) + 1
print(type(var1))
print(var1)