
'''
d = {'a':'apple', 'b':'banana', 'c':'car', 'd': 'desk'}
for key in d:
  # 遍历字典时遍历的是键
  print(key, d.get(key))
# for key, value in d.items():
# 上下两种方式等价 d.items() <=> dict.items(d)
for key, value in d.items(): # dict.items(d):
  print(key, value)

s = 'I love you more than i can say'
for i in s:
  print(i)
'''

list1 = ['饼子','瀚儿','关生','小李','小陈','小罗']

for name in list1:
    if name == "小李":
        break
    print(name)
    print('*' * 10)


for name in list1:
        if name == "小陈":
            continue
        print(name)

list3 = []
list4 = [99,100]
for i in range(10):
    if i >= 0:
        list3.append(i)
list4.extend(list3)
print(list4)

#
for cici in range(0,10,3):
    print(cici)

'''
参数定义的类型：
1.必备参数：定义了就必须要传入的参数——不传会出错
2.默认参数（缺省参数）：可以定义的时候赋值一个默认值 —— 调用的时候可以不传入；可以传入替换掉默认值
注意：默认参数必须在必备参数后面！！
3.不定长参数：等前面的必备参数和默认参数都接受完了，剩下的参数都不给不定长参数接受,顺序不能乱
接受不确定数量，个数的参数 —— 可以不传 ， 可以传入（1,多个） 
*args:按照位置接收 == 元组接收
**kwargs:按照参数 == 字典接收
'''

'''
def good_job(salary,bonus,subsidy=500,*args,**kwargs):
    sum1 = salary + bonus + subsidy
    print("salary的值：{}".format(salary))
    print("bonus的值：{}".format(bonus))
    print("subsidy的值：{}".format(subsidy))
    print("args的值：{}".format(args))
    print("kwargs的值：{}".format(kwargs))
    for i in args:
        sum1 += i
    for j in kwargs:
        # sum1 += kwargs.get(j)
        sum1 += kwargs[j]

    print("这个工作的工资总和是：{}".format(sum1))
good_job(8000,2000,580,50,1000,200,a=33,b=23,rr=23)

list5 = [1,99,55,66,77,22]
print(list5[2])

'''

def good_job(salary,bonus,subsidy=500,*args,**kwargs):
    sum1 = salary + bonus + subsidy
    for i in args:
        sum1 += i
    for j in kwargs:
        # sum1 += kwargs.get(j)
        sum1 += kwargs[j]
    return sum1

result = good_job(8000,200,2000)
if result > 10000:
    print('这工作真香')
else:
    print("不干了，淦")
'''
lis5 = []
str2 = 'I love you'
for s in str2:
    if s != 0:
        lis5.append(s)
print(lis5)

lis6 = [list(str2)]
print(lis6)
print(lis6[0])
print(str(lis5))
'''
strsb = '12345'
list2 = (list(strsb))
print(list2)

strsa = 'I love you baby test you'
lissa = list(strsa)
lissb = strsa.split(' ')
lissc = strsa.split(" ",2)# split（?,N）n是以?为分割点的最大次数，如果没有数字限制，则一直以"?"的形式分割
print(lissa)
print(lissb)
print(lissc)

a = ['I','love','you']
b = ' '.join(a)
print(b)

c = ['I','love','you',3000]
d = map(str,c) #有 int 常数，不能直接用 join函数，需要用map先转换
e = ' '.join(d)
listf = list(e)
print(e)
print(listf)

def function_len(object):
    # if type(object) == dict or type(object) == list or type(object) == str:
    if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):
        leng =len(object)
        if leng >= 5:
            print('True')
        else:
            print('False')
    else:
        print("数据类型不能计算长度")

function_len("sdad")

