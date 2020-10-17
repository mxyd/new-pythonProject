#继承
#创建一个父类
class Father:
    def __init__(self,money,hourseName,car):
        self.money = money
        self.hourse = hourseName
        self.car = car

#创建一个子类--完全继承父类
class Son1(Father):
    pass

S1 = Son1(1000,"别墅","infinity")
# print(f"我有{S1.money}$,开的是{S1.car},住的是{S1.hourse}")

#创建一个子类，子类里面有与父类不相同的属性
"""
#1--lover--子类自己的属性-- 将自己的私有属性和父类的属性写在子类的init 方法里面
#2--使用 父类名.__init__(父类的属性) 或者使用super().方法名(),方法名里面不要写self
"""

class Son2(Father):

    #1--lover--子类自己的属性-- 将自己的私有属性和父类的属性写在子类的init 方法里面
    def __init__(self,money,hourseName,car,lover):

    #2--使用 父类名.__init__(父类的属性)，这个init()里面需要写上self， 或者使用super().方法名(),方法名里面不要写self

        Father.__init__(self,money,hourseName,car)

        # super().__init__(money,hourseName,car)
        self.lover = lover
s2 = Son2(1000,"别墅","infinity","李思思")
# print(f"我有{s2.money}$,开的是{s2.car},住的是{s2.hourse},喜欢的是{s2.lover}")





"""
商城类：
vip用户--类：
权限：折扣8折，生日券，礼品券
购买行为：全国包邮

SVIP用户--类  入会费：600
权限：折扣8折，生日券，礼品券，金额 ，理财服务
购买行为：全国包邮+礼品--一年5次机会
"""
#vip用户类
class Vip():
    welfare = "折扣8折+生日券礼品券"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def shopping(self):
        print("全国包邮")
#svip用户类
class Svip(Vip):
    def __init__(self,name,age,level):
        super().__init__(name,age)
        self.level = level
    #vip用户的shopping方法不能满足svip用户的权限，所以要重写这个  shopping()
    def shopping(self):
        print("全国包邮+礼品--一年5次机会")
##------------选择登陆级别----

userLevel = input("vip用户请输入: 1 ；svip用户请输入: 2:")
if userLevel == '1':
    name,age = input("用户名,年龄").split(',')#---用户名,年龄组成的一个list--list[输入的用户名,年龄]
    vip1 = Vip(name,int(age.strip()))
    vip1.shopping()
elif userLevel == '2':
    name,age,level = input("请输入：用户名,年龄,等级").split(',')
    svip1 = Svip(name,int(age.strip()),int(level.strip()))

    if int(level) > 2:
            print("Svip 用户只有三次购物的机会已使用完毕")
            super(Svip,svip1).shopping()
    else:
        svip1.shopping()

else:
    print("---此用户无权限----")

