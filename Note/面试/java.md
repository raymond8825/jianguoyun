# 1. 手写单例模式
懒汉模式
```java
public class Singleton {
    private static Singleton singleton;
    private Singleton() {}
    public static Singleton getInstance() {
        if (singleton == null) {
            singleton = new Singleton();
        }
        return singleton;
    }
}
```
# 2. 多线程中，i++是线程安全的吗？
# 3. String和StringBulider和StringBuffer的区别
当对字符串进行修改的时候，需要使用 StringBuffer 和 StringBuilder 类。

和 String 类不同的是，StringBuffer 和 StringBuilder 类的对象能够被多次的修改，并且不产生新的未使用对象。

StringBuilder 类在 Java 5 中被提出，它和 StringBuffer 之间的最大不同在于 StringBuilder 的方法不是线程安全的（不能同步访问）。

由于 StringBuilder 相较于 StringBuffer 有速度优势，所以多数情况下建议使用 StringBuilder 类。然而在应用程序要求线程安全的情况下，则必须使用 StringBuffer 类。
# 4. Integer和int有什么区别
Integer 是对象类型 int是原始类型 适用场合有很大的不同 之所以要把int封装成Integer 型 是因为很多方法参数就只接收对象类型(Object) 还比如 范型 就只支持 对象类型
Integer必须实例化才能使用，默认值为null，int则不需要实例化，默认值为0;
# 5. final，finally，finalize的区别
final：java中的关键字，修饰符。
A).如果一个类被声明为final，就意味着它不能再派生出新的子类，不能作为父类被继承。因此，一个类不能同时被声明为abstract抽象类的和final的类。
B).如果将变量或者方法声明为final，可以保证它们在使用中不被改变.
　　1)被声明为final的变量必须在声明时给定初值，而在以后的引用中只能读取，不可修改。
　　2)被声明final的方法只能使用，不能重载。
finally：java的一种异常处理机制。
　　finally是对Java异常处理模型的最佳补充。finally结构使代码总会执行，而不管无异常发生。使用finally可以维护对象的内部状态，并可以清理非内存资源。特别是在关闭数据库连接这方面，如果程序员把数据库连接的close()方法放到finally中，就会大大降低程序出错的几率。
finalize：Java中的一个方法名。
Java技术使用finalize()方法在垃圾收集器将对象从内存中清除出去前，做必要的清理工作。这个方法是由垃圾收集器在确定这个对象没被引用时对这个对象调用的。它是在Object类中定义的，因此所的类都继承了它。子类覆盖finalize()方法以整理系统资源或者执行其他清理工作。finalize()方法是在垃圾收集器删除对象之前对这个对象调用的。
# 6. mysql中创建含有id，ip，时间的表，并插入一条当前ip和当前时间
```sql
create table test(
    id int primary key auto_increment,
    ip varchar(20),
    time DATETIME
);
```
# 7. 什么是线程安全
线程安全就是说多线程访问同一代码，不会产生不确定的结果。编写线程安全的代码是低依靠线程同步。
# 8. java常用工具类
String 字符串类
System 可得到系统信息
StringBuilder 字符串工具类
Thread 线程类
Math 与数学有关的工具类
ArrayList 底层用数组实现的集合
LinkedList 底层用链表实现的集合
HashMap 接口Map的一个实现类
HashSet 接口Set的一个实现类
Scanner 简单文本扫描器
Calendar 日期类
Date 日期类
File 目录或文件操作类
FileInputStream 输入流
FileOutputStream 输出流

