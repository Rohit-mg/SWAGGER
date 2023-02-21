# sum =0
# flag = True
#
# while(flag):
#     user_input = input("enter the digits and q to quit")
#     if user_input != 'q':
#         sum +=int(user_input)
#         print(sum)
#     else:
#         print(sum)
#         flag = False
# #
# #
#
# #factorial
# def fact(num):
#     fact = 1
#     # num = int(input("enter a no."))
#     while(num>1):
#         fact*=num
#
#         num-=1
#     fact = reversed(str(fact))
#     return fact
#
# def zero_trail(fact):
#     count = 0
#     for x in fact:
#         if x =='0':
#             count+=1
#         else:
#             break
#     print(count)
#
# # zero_trail(fact(7))
#
#
# num =123
#
# while(num>1):
#     a = int(num%10)
#     print(a)
#     num = num/10
#     print(int(num))



# with open('currency_data.txt') as f:
#     lines = f.readlines()
# print(lines)
#
# dict = {}
# for line in lines:
#     parse = line.split('\t')
#     dict[parse[0]] = parse[1]
#
# value = int(input("enter a value"))
# print(dict.keys())
# c_val = input("enter the currency u want to convert to ")
# num = float(dict[c_val])
# print(num*value)


# s = [4,34,43,43,2,32133]
# y = []
# for x in s:
#     t = str(x)
#     print(t)
#     y.append(t)
# print(y)
# print("r".join(y))







# str(fact)
# print(type(fact))
# print("Type of variable before conversion : ", type(fact))
#
# # convert the num into string
# converted_num = str(fact)
#
# # check  and print type converted_num variable
# print("Type After conversion : ", type(converted_num))
# l =[]
# for n in converted_num:
#     l.append(n)

# l = ["rohit","bohit","mohit"]
# for i,x in enumerate(l):
#     if(i%2==0):
#
#         print(i,x)
#     else:
#         pass
# d =[]
# d.append(" ".join(l))
# print(d)
#
# for i in l:
# #     print(i,end="*")
#
# a = lambda sq :sq + 10
# print(a(3))
#
#
# def sqa(n):
#     return n>5
#
# def cub(m):
#     return m*m*m
#
# li = [sqa,cub]
# lis = [1,2,3,4,5,6,7,8,9]
#
#
# lis  = list(map(sqa,lis))
# lis1 = list(filter(sqa,lis))
# print(lis)
# print(lis1)
#
#
# class emp :
#
#     idd = 1
#
#     def __init__(self,name,age,sal):
#         self.name = name
#         self.age = age
#         self.sal = sal
#
#     def bonus(self):
#         return self.sal+10%(self.sal)
#
#     @classmethod
#     def sal_ch(cls,sall):
#         cls.idd = sall
#
#     @staticmethod
#     def func():
#         return "i was called by the object"
#
#
# e1 = emp("rohit",22,202020)
# e2 = emp("mohit",23,534784)
# increment = e1.bonus()
# print(increment)
# e2.sal_ch(4000000)
# print(e1.idd)
# print(e1.func())
# print(e2.idd)




class a:

    def deco(func):
        def check(self,no):
            print('deco start')
            func(self,no)
            print('done')
        return check

    @deco
    def func1(self,no):
        print("class a i'm the no",no)
class b(a):
    @a.deco
    def func2(self,no):
        print ("class b no=",no)



B = b()
B.func2(60)
print("\n")
A = a()
A.func1(90)







