# -*- coding: UTF-8 -*-
# @Mingway.Hu
print "================"
print "|  Calculator  |"
print "================"


jia=lambda x,y:x+y
jian=lambda x,y:x-y
cheng=lambda x,y:x*y
chu=lambda x,y:x/y

dic = {'+':jia,'-':jian,'*':cheng,'/':chu}
d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0,".":"p",}
 
def pd(num):  #判断input的是否为实数
    a = 0
    b = 0
    for i in num:
        if i == ".":
            a += 1
        if i not in d or a > 1:
            b = False
            break
        else:
            b = True
    return b
 
def cal():    #进行运算
    x = raw_input("Please input a number (X) : ")
    while not pd(x) :
        x = raw_input('Not a correct number, please input (X) again: ')
       
    opt = raw_input("Please input a operator (Option) such one as '+' , '-' ,'*' or '/': ")   
    while opt not in dic : #判断运算符号
        opt = raw_input('Not a given operator, please input (Option) again: ')
       
    y = raw_input("Please input the other number (Y): ")
    while not pd(y):
        y = raw_input('Not a correct number, please input (Y) again: ')
    if float(y) == 0.0 and opt == '/':
        print 'Y cannot be zero when option is "/", please input all number again!'
        return cal()

    result = str(dic.get(opt)(float(x),float(y))) #计算用户想要的结果
    if result[(len(result)-2):len(result)] == ".0" : #判断结果是否是带有小数位的整型
        print "Result: %s"  %result[:(len(result)-2)]
    else:
        print "Result: %s" %result
    return cal

if __name__ == '__main__':
   cal()
