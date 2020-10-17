# 2020/10/15
# author:xieyudong
#创建一个类---类名首字母必须大写
class Person():
    #创建一个静态属性--其实就是一个在类里面的变量
    pepole = "人类"
    #创建一个实例属性--其实就是 init() 函数里面的形参--实例属性最好放在 __init__() 方法里面
    #如果此属性在每个实例里面展示的都不一样，就用实例属性
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    #--------------创建实例方法------------------
    #创建一个实例方法--其实就是在类里面创建一个函数---通过实例调用
    #判断方法和实例属性是否相关，相关话，就创建实例方法
    def eat(self):
        self.weight +=10
        print(f"{self.name}吃饭了，体重是{self.weight}")


    # --------------创建类方法------------------
    #创建一个类方法--在方法前使用@classmathod声明，使用 类名.方法名()或者 实例.方法名()
    #作用  可以修改静态属性
    @classmethod
    def tell(cls):
        cls.pepole = "人类呀"
        print("我是实例方法")
        return cls.pepole

    # --------------创建静态--就是类里面的一个普通函数------------------
    @staticmethod #和类不相干的方法或者其他操作可以放到静态方法里面
    def run(num):
        # print(f"{Person('tom',20,100).pepole}能跑{num}km")
        # print(f"能跑{num}km")
        return (f"{Person('tom',20,100).pepole}能跑{num}km")
#**********实例方法调用**********
#创建类的实例---其实就是类的调用 1--类名() 2--  变量=类名()
#创建类的实例后，会自动调用 init()方法
p1 = Person("tom",20,100)
# print(p1.name)
# p1.eat()

#**********类方法调用**********
print(Person.tell())#类名调用
# print(p1.tell())# 通过实例调用

#**********静态方法调用**********
# print(Person.run(10))
print(p1.run(10))






