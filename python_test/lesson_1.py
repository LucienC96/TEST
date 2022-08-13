
'''
多行注释
试一下
'''
# 三引号可以保持格式
# 单行注释
# ctr + / 快捷注释  且 快捷取消注释
# \  为转义符

print('''俺媳妇罗思''')

# 标识符不可以 空格、 数字、除下划线以外的的符号 作为开头
# 变量：存储数据的 == 保险柜：钱，金条——存储东西
# 数据类型：int float bool str
# 变量名：标识符 —— 1,2,3,4
# 变量名一定要先声明（定义并赋值）

info = "我老婆是罗思思"
name = "cici"

print(name)

# 字符串的操作：
# 1、取值：元素 位置 —— 索引，从零开始，依次加一
# 2、取多个值：切片 —— [开始：结束：步长]===取头不取尾
#

str1 = "hello world!"
str2 = str1[2:5:1]
print(str2)
print(str1.find("w"))
print(str1.count("l"))

# 格式化输出：
# 第一种1.占位符{}  2.默认顺序,指定和默认顺序不能混用，变黄
# 第二种：%s 字符串 == 匹配所有 %d--整数  %f--小数
name = "cici"
age = "18"
hobby = "lucien"

print('''
---{1}---
name:{1}
age:{0}
hobby:{2}

'''.format(age,name,hobby))

'''
python运算符：+ - * / % **
赋值运算符：= += -=：方向性 ---右边赋值左边
比较预算符：< <= > >= == != ----- 运算结果是布尔值 True False
比较运算符：与-and== 真真为真 或--or==假假为假 非-not 运算结果是布尔值 True False
成员运算符：in, not in 运算结果是布尔值 True False
'''
print(10 + 20)
print("love"+" cici")
print(str(666)+"cici")

list1 = [20,3.14,True,"媳妇儿",[1,2,3],False,'test','xuxu','cici']
print(list1)

list1.pop(5)
list1.remove(20)
list1.insert(0,20)
del list1[2:5]
list1.append('30')
list2 = [55,65]
list1.extend(list2)

#del 只能删除变量，不能删除数据 1为对象（数据），a=1 对象1被a变量引用
# list[1,2,3],本身不包含数据1 2 3，而是包含变量list[0],list[1]

print(list1)

aa = list1.clear()
print(aa)

tuple1 = ('asdasd',255,31,'嗨咯') #tuple元组,对象不可改变
print(tuple1)
list2 = list(tuple1)
list2[-1] = "小丑"
print(list2)
tuple2 = tuple(list2)
print(tuple2)

'''
字典：dict {}
1，元素： key：value
2，场景： 存储数据属性：人——名字 身高 体重
key：1）不能是改变的数据类型（list，dict）—— 字符串
     2）不能重复，唯一
value：可以是任意数据类型 —— 可以被改变 == 增删改
3，字典是没有顺序的！ 不能索引取值  取值：通过key 取value
'''
dict1 = {"name ":"lucien","height":"173","weight":170,"age":"18","test":"test1"}
print(dict1["height"])
print(dict1.get("weight"))
dict1["weight"] = "150"
print(dict1)
dict1.pop("age") #需要指定key删除，与list不同
del dict1["test"]
print(dict1)

dict1.update({"age":"18","city":"shenzhen","hobby":"cici"}) #key名不能重复
print(dict1)

'''
集合 set {}，元素单个
1.无序
2.元素不可以重复 —— 使用场景：去重
'''
list3 = [11,22,11,33,44,55,33]
set1 = set(list3)
print(set1)

'''
控制流：代码执行顺序-- 从上至下一次执行：判断 循环
判断：if 语法
if 条件：—— 成立 —— 冒号：缩进（4个空格 tab键）
elif 条件： —— 成立
    执行语句（子代码）
……（elif可以没有，可有多个）
else：—— 可以没有
    执行语句
'''
print("---------------作业时间-------------------")

a = [1,6,'cici','summer']
print('i' in a)

dict_1 = {"class_id":45,'num':20}
if dict_1['num'] > 5:
    print(dict_1["num"])

money = int(input("请输入你的你余额")) #input()控制台输入——数据类型——字符串

if money >= 500:
    print("买别墅")
elif money >= 200:
    print("买房")
elif money >= 50:
    print("买车")
else:
    print("滚去工作")

name= input("请输出你的名字：")
gender = input("请输入你的性别：")
age = input("请输入你的年龄：")
print("*" * 20)
print('''name:{}
gender:{}
age:{}
'''.format(name,gender,age))




