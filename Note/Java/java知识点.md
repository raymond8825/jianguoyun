# 1 类和对象
## 1.1 包package
把比较接近的类，规划在同一个包下，使用同一个包下的其他类，直接使用即可，但是要使用其他包下的类，必须用import
## 1.2 访问修饰符
# 2 多线程
## 2.1 创建多线程
创建多线程有3种方式，分别是继承线程类,实现Runnable接口,匿名类
## 2.1.1 通过继承线程类创建多线程
首先要专门多写出一个用来处理事务的类比如叫做AttackThread，表示创建该线程用来完成攻击线程。这个类里声名的属性是用来存储将要处理的事务所涉及的对象，通过类的构造方法来给属性赋值，然后具体事务的处理就放入到该类重写Thread类中的run方法，然后在main函数中创建AttackThread对象，后调用该对象的start方法完成线程的启动。然后多创建几个AttackThread对象，就可以运行多线程程序了。
## 2.1.2 通过实现Ruunable接口创建多线程
此种方法也需要额外建立一个类AttackThread，但是这个类实现Runnable接口并实现run方法（这里和第一种方法并不一样），别的和第一种方法一样，需要创建属性来接收事务涉及的对象，对象的赋值通过该类的构造方法，事物的执行在run方法中。在main方法中，创建一个AttackThread对象at，但是由于该类仅仅实现了Runnable方法，没有属于Thread的start方法启动线程，所以需要用`new Thread(at).start();`来执行多线程。
## 2.1.3 通过匿名类创建多线程
使用匿名类，继承Thread,重写run方法，直接在run方法中写业务代码
匿名类的一个好处是可以很方便的访问外部的局部变量。
前提是外部的局部变量需要被声明为final。(JDK7以后就不需要了)

直接在main函数中创建一个Thread对象，比较复杂，[到这里看](http://how2j.cn/k/thread/thread-start/353.html#nowhere)

## 2.2 线程常见的方法
sleep,join<sup>?</sup>(不懂有什么意义) ,setPriority,yield(这里只是介绍了临时暂停线程，python中的迭代器应该有讲)
## 2.3 多线程同步问题
多线程的同步问题指的是多个线程同时修改一个数据的时候，可能导致的问题

多线程的问题，又叫Concurrency（并发） 问题

1. 第一种解决并发方法
```java
Object someObject =new Object();
Thread t=new Thread(){
    public void run(){
        synchronized (someObject){
  //此处的代码只有占有了someObject后才可以执行
}
    }
}
```
synchronized表示当前线程，独占 对象 someObject
当前线程独占 了对象someObject，如果有其他线程试图占有对象someObject，就会等待，直到当前线程释放对someObject的占用。
someObject 又叫同步对象，所有的对象，都可以作为同步对象
为了达到同步的效果，必须使用同一个同步对象

释放同步对象的方式： synchronized 块自然结束，或者有异常抛出

2. 第二种解决并发问题
直接在方法前面加上synchronized修饰符
```java
    //回血
    //直接在方法前加上修饰符synchronized
    //其所对应的同步对象，就是this
    //和hurt方法达到的效果一样
public class Hero{
        public synchronized void recover(){
        hp=hp+1;
    }
     
    //掉血
    public void hurt(){
        //使用this作为同步对象
        synchronized (this) {
            hp=hp-1;   
        }
    }
} 
```
## 2.4 线程安全类
如果一个类，其方法都是有synchronized修饰的，那么该类就叫做线程安全的类

同一时间，只有一个线程能够进入 这种类的一个实例 的去修改数据，进而保证了这个实例中的数据的安全(不会同时被多线程修改而变成脏数据)
## 2.5 线程之间的交互
当两个线程之间需要进行交互通知，即为线程一什么时候暂停等待并释放资源对象this(this.wait()--->让占有this对象的线程一暂停并释放对象this)，此时另外一个线程二便可以调用该对象this，当线程二调用完毕后，通过this.notify()方法通知正在等待this的线程一苏醒过来

> 线程暂停的时候一定要加上异常捕获,比如
> ```java
> try
> {
> this.wait();
> }catch(InterruptedException e)
> {
>   e.printStackTrace();
> }
> 
> ```

这里需要强调的是，wait方法和notify方法，并不是Thread线程上的方法，它们是Object上的方法。

因为所有的Object都可以被用来作为同步对象，所以准确的讲，wait和notify是同步对象上的方法。

wait()的意思是： 让占用了这个同步对象的线程，临时释放当前的占用，并且等待。 所以调用wait是有前提条件的，一定是在synchronized块里，否则就会出错。

notify() 的意思是，通知一个等待在这个同步对象上的线程，你可以苏醒过来了，有机会重新占用当前对象了。

notifyAll() 的意思是，通知所有的等待在这个同步对象上的线程，你们可以苏醒过来了，有机会重新占用当前对象了。
 步骤 4 : 练习-线程交互     
## 2.6 线程池
每一个线程的启动和结束都是比较消耗时间和占用资源的。

如果在系统中用到了很多的线程，大量的启动和结束动作会导致系统的性能变卡，响应变慢。

为了解决这个问题，引入线程池这种设计思想。
