# 1. spring 是什么 
Spring是分层的 Java SE/EE应用 full-stack 轻量级开源框架，以 IoC（Inverse Of Control： 反转控制）和 AOP（Aspect Oriented Programming：面向切面编程）为内核
# 2.两大核心IOC和AOP
## 2.1 IOC
反转控制：接触代码中的依赖关系

## 2.2 AOP
# 3.spring是如何工作的
通过修改配置文件来降低文件的耦合性，其中通过bean来让spring创建对象。
## 3.1 spring依赖注入（DI）
spring可以通过bean来创建对象，但是如何让spring在创建的时候就给对象赋值了呢？此时用用到DI
### 3.1.1 set方法注入（最重要）
就是在类中提供需要注入成员的 set 方法，然后在xml配置文件中仍然要修改，需要在bean中添加property节点，值类型就是给name，value属性赋值，引用类型就是name，ref赋值，其中二者的name都是自己想写啥写啥
### 3.1.2 构造函数注入
### 3.1.3 使用p名称空间注入
## 3.2 注入集合属性
，就是给类中的集合成员传值，它用的也是set方法注入的方式，只不过变量的数据类型都是集合。 我们这里介绍注入数组，List,Set,Map,Properties