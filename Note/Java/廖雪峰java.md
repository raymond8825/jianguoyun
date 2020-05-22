# 1. java核心类
## 1.1 字符串String
String也是一个类，但是因为String太常用了，所以Java提供了"abc"这种字符串字面量表示方法。

Java字符串的一个重要特点就是字符串不可变。这种不可变性是通过内部的private final char[]字段，以及没有任何修改char[]的方法实现的。

java中字符串比较是否相同的时候使用的equals()方法，如果使用==比较的是两个对象的地址

java中str.replaceAll("[\\,\\;\\s]+", ",")方法是使用正则表达式来替换，而不同于str.replace()

java中的字符串都是为Unicode编码
## 1.2 StringBuilder和StringBuffer
由于使用String类型拼接字符串时候每次都需要重新创建新的字符串，抛弃旧的引用，创建了很多临时对象（不过最新版本的jvm已经在编译的时候将这种情况的String对象编译为类似StringBuilder的对象）导致给GC带来了比较大的压力，遍引入了StringBuilder类。该类是一个可变对象，在StringBuilder对象新增字符的时候并不会新增临时对象

- StringBuffer是StringBuilder的线程安全版本，但是线程安全意味着要消耗更大的性能，随着jvm的优化，现在没有什么必要去使用StringBuffer（怎么优化）
## 1.3 StringJoiner（import java.util.StringJoiner）
高效拼接字符串使用StringBuilder的确不错，但是对于常见的场景：用分隔符分隔数组，使用StringBuilder时还需要在for循环之后删除末尾上的分隔符，非常不方便，所以有了StringJoiner。可以为StringJoiner对象专门设置开头和结尾，所以拼接很方便，该类内部实现了StringBuilder,所以拼接效率和StringBuilder是一致的
## 1.4 包装类型
首先java有基本数据类型和引用数据类型，引用类型可以赋值为null，而基本类型则不可以，怎么将基本类型转换为引用类型呢？用到了包装类。
```java
Integer n = 100; // 编译器自动使用Integer.valueOf(int)
int x = n; // 编译器自动使用Integer.intValue()
```
而jvm会自动为我们实现拆装箱，但是自动拆装箱仅仅是为了少写代码，但是却换来了由于拆装箱导致的性能下降。


```java
public class Main {
    public static void main(String[] args) {
        Integer x = 127;
        Integer y = 127;
        Integer m = 99999;
        Integer n = 99999;
        System.out.println("x == y: " + (x==y)); // true
        System.out.println("m == n: " + (m==n)); // false
        System.out.println("x.equals(y): " + x.equals(y)); // true
        System.out.println("m.equals(n): " + m.equals(n)); // true
    }
}
```
仔细观察结果的童鞋可以发现，==比较，较小的两个相同的Integer返回true，较大的两个相同的Integer返回false，这是因为Integer是不变类，编译器把Integer x = 127;自动变为Integer x = Integer.valueOf(127);，为了节省内存，Integer.valueOf()对于较小的数，始终返回相同的实例，因此，==比较“恰好”为true，但我们绝不能因为Java标准库的Integer内部有缓存优化就用==比较，必须用equals()方法比较两个Integer。

因为Integer.valueOf()可能始终返回同一个Integer实例，因此，在我们自己创建Integer的时候，以下两种方法：

- 方法1：Integer n = new Integer(100);
- 方法2：Integer n = Integer.valueOf(100);

方法2更好，因为方法1总是创建新的Integer实例，方法2把内部优化留给Integer的实现者去做，即使在当前版本没有优化，也有可能在下一个版本进行优化。

我们把能创建“新”对象的静态方法称为静态工厂方法。Integer.valueOf()就是静态工厂方法，它尽可能地返回缓存的实例以节省内存。
> 创建新对象时，优先选用静态工厂方法而不是new操作符。


Java核心库提供的包装类型可以把基本类型包装为class；

自动装箱和自动拆箱都是在编译期完成的（JDK>=1.5）；

装箱和拆箱会影响执行效率，且拆箱时可能发生NullPointerException；

包装类型的比较必须使用equals()；

整数和浮点数的包装类型都继承自Number；

包装类型提供了大量实用方法。（进制转换，类型转换，大小比较之类的
## 1.5 JavaBean
## 1.6 Enum枚举类型
Enum本身也是一个class类型的，当我们使用类型比较的时候要使用equals()方法，如果使用==比较，它比较的是两个引用类型的变量是否是同一个对象（即为比较两个对象的地址）。因此，引用类型比较，要始终使用equals()方法，但enum类型可以例外。
这是因为enum类型的每个常量在JVM中只有一个唯一实例，所以可以直接用==比较：当然我们依然可以使用`equals()`方法，但是却需要更多的代码。

既然enum定义的枚举类也是个class，和其他class有什么区别？
答案是没有区别。
## 1.7 BigInteger
java中内置了最大整数支持long类型64位，支持直接在cpu内部进行运算，速度很快。但是我们需要更大的位数的时候，使用`java.math.BigInteger`类，可以表示大整数，但是运行速度则要慢很多。
### 1.7.1 BigInteger类型转换
- 转换为byte：byteValue()
- 转换为short：shortValue()
- 转换为int：intValue()
- 转换为long：longValue()
- 转换为float：floatValue()
- 转换为double
把BigInterge类型转换为基本类型，但是当BigInterge数值过大时在转换的时候
