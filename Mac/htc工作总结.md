# 1. @RequestMapping(vaule=""/get_date_reconcilation", method = RequestMethod.GET")
@RequestMapping注解来将请求URL映射到整个类上或某个特定的方法上，即@RequestMapping 既可以定义在类上，也可以定义方法上。
# 2. @RequestParam(value="" long parkId)
```java
public String getDateReconcilation(HttpServletRequest request,
@RequestParam(value = "parkId")   long parkId)
```
@RequestParam用于将请求参数区数据映射到功能处理方法的参数上
- parkId:是停车场的所有者
# 3. Google Guava
# 4. IDEA中全局搜索
`command + shift + f`
# 5. JAVA的方法参数中传入的数据类型后面有三个点
表示可以传入不定参数，参数的个数不一定，当传入较多参数的时候，采用数组来接收
# 6. RequestParam和RequestBody
注解@RequestParam接收的参数是来自requestHeader中，即请求头。通常用于GET请求，像POST、DELETE等其它类型的请求也可以使用。

注解@RequestBody接收的参数是来自requestBody中，即请求体。一般用于处理非 Content-Type: application/x-www-form-urlencoded编码格式的数据，比如：application/json、application/xml等类型的数据。通常用于接收POST、DELETE等类型的请求数据，GET类型也可以适用。
# 7. ps -ef | grep mysql
ps命令将某个进程显示出来

grep命令是查找

中间的|是管道命令 是指ps命令与grep同时执行

PS是LINUX下最常用的也是非常强大的进程查看命令

grep命令是查找，是一种强大的文本搜索工具，它能使用正则表达式搜索文本，并把匹配的行打印出来。

grep全称是Global Regular Expression Print，表示全局正则表达式版本，它的使用权限是所有用户。

以下这条命令是检查java 进程是否存在：ps -ef |grep java

字段含义如下：(此处可以去看md的源文件，只是位置没有对上而已)

UID       PID       PPID      C     STIME    TTY       TIME         CMD

zzw      14124   13991      0     00:38      pts/0      00:00:00    grep --color=auto dae



UID      ：程序被该 UID 所拥有

PID      ：就是这个程序的 ID 

PPID    ：则是其上级父程序的ID

C          ：CPU使用的资源百分比

STIME ：系统启动时间

TTY     ：登入者的终端机位置

TIME   ：使用掉的CPU时间。

CMD   ：所下达的是什么指令
# 8. 什么是shell？
Shell 是一个应用程序，它连接了用户和 Linux 内核，让用户能够更加高效、安全、低成本地使用 Linux 内核，这就是 Shell 的本质。，shell和普通的迅雷，qq并没有什么区别

# 9. 关于BigDecimal的大小比较问题
BigDecimal类型不能直接进行+ - * / 运算，必须要在要用BigDecimal类中的方法来进行比较，因为BigDecimal精度较高，所以用方法来比较大小。
## 9.1 相等时

## 9.2 计算差值

# 10. boolean转换为int类型
不能用int()强制转换，而是应该使用
```java
int i = true ? 1 : 0;
```

# 11. `\u0001`或者`\1`
`\u0001`和`\1`在java中都表示一个不可见且不站位置的反义字符，二者是相等的。常用来分隔自己拼接的字符串
```java
public class Test {
    public static void main(String[] args) {
        // d3fe1e186e41475ea965f4722f5488a8\\15093\\1公共设施
        String str1 = "字段A";
        String str2 = "字段B";
        String str3 = "字段C";

        String str = str1 + "\1" + str2 + "\1" + str3;
        System.out.println(str);
        // 也就是下面的字符串，分隔符为 \u0001
        //str = "d3fe1e186e41475ea965f4722f5488a8\u00015093\u0001公共设施";
        String[] split = str.split("\1");
        for (String s : split) {
            System.out.println(s);
        }
        System.out.println(split.length);
    }
}

```
# 12. String.valueOf(str)
在读取数据时需要对数据的强制转换，可采用String.valueOf(a)，把a强制转换成字符串类型

有时候a本来就已经是字符串类型了，但是为了代码的严谨性，也会加入String.valueOf(a)，这时String.valueOf(a)省略也不会出错的。

当object为null 时，String.valueOf（object）的值是字符串”null”，而不是null

# 13. 根据文件名字进行查询
[详细教程](https://blog.csdn.net/fungleo/article/details/78489552)
- 第一种方法（支持reg）：`find ./ -name 正则表达式`
- 第二种方法（更简单）：`find ./ | grep 文件名字`
# 14. int转long和Long
int转long直接使用`(long)5`，int转为Long时首先将int转为long类型，然后使用`new Long((int)5)`
# 15. 其他类型转String,Long等类型的时候
使用String.valusOf(i)或者Long.valueOf(i)
# 16. Postman调试接口
当接口采用post请求时，url处只有接口的名字却没有请求参数，具体的请求参数位于post请求总body中，里面可能为json模式（在postman中使用raw，然后选择json模式），也可能为form-data格式，具体可以在chrome中的RequestBody中可以知道是哪一种模式。
# 17. 获得前端窗口的数据
首先需要建立一个接收前端传来数据的类，在参数中使用`@RequestBody`来传给刚才建的类进行赋值。

# 18. BigDecimal中保留两位小数
```java
package alipay.fund.trans.toaccount;

import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.text.NumberFormat;
public class demo {
    double f = 41.20999999999998;
    public void m1() {
        BigDecimal bg = new BigDecimal(f);
        double f1 = bg.setScale(2, BigDecimal.ROUND_HALF_UP).doubleValue();
        System.out.println(f1);
    }
    /**
     * DecimalFormat转换最简便,
     */
    public void m2() {
        
        DecimalFormat df = new DecimalFormat("0.00");
        System.out.println(df.format(f));
    }
    /**
     * String.format打印最简便
     */
    public void m3() {
        System.out.println(String.format("%.2f", f));
    }
    public void m4() {
        NumberFormat nf = NumberFormat.getNumberInstance();
        nf.setMaximumFractionDigits(2);
        System.out.println(nf.format(f));
    }
    
    // 主方法
    public static void main(String[] args) {
    	demo f = new demo();
        f.m1();
        f.m2();
        f.m3();
        f.m4();
    }
}
```
# 19. IDEA中将代码提取为方法
`Command+Option+M`
# 20. sql中datetime和timestamp的区别
他们在数据库显示的格式都是一样的YYYY-MM-DD-HH-MM-SS,但是datetime适合记录创建时间，但是timestamp适合记录更新时间，因为系统会自动给timestamp赋值。 *其中date类型是显示年月日，而time类型是时分秒。*
[详细概述sql中datetime和timestamp的区别](https://blog.csdn.net/qq_27950699/article/details/88532805)
# 21. sql如何怎样把查询的结果保存成一张临时表(尝试失败)
插入的方式有多种，下面介绍常用的2种：

1. 先不声明，直接在SQL中插入，SQL 如下：
```sql
select test into #Temp from table
```

查询完成，记得
```sql
drop table #temp
```

2. 先创建临时表，SQL 如下：
```sql
create table #Temp （Test nvarchar（50））

insert into #temp  select test from table
```
# 22. git pull 和git pull --rebase的区别
当我们开发了一个新的版本并commit之后，发现本地和git仓库出现分支的时候,[详情](https://blog.csdn.net/qq_37708668/article/details/88813266)
1. `git pull --rebase`
2. 如果出现冲突，则修改完毕冲突，使用`git add .`来增加索引，然后使用`git rebase --continue`合并分支就可以`git push`
3. 千万不要使用`git rebase --skip`:则会将引起冲突的commits丢弃掉（慎用！！）
# 23. 多表（两表及两表以上）查询中多表之间有重复的字段
```sql
select * from slot_renewal_record
join slot slo on slo.id = slot_renewal_record.slot_id
join operator ope on slot_renewal_record.operator_id=ope.id where slot_renewal_record.park_id = 1 and slot_renewal_record.valid > 0 and slo.show_status = 1 and ope.name like "%luoqijun%" limit 0, 99;
```
这三个表每个表都有一个`created_at`时间，而且排列顺序是|slot_renewal_record|slot|operator|,但是我们想要`slot_renewal_record.created_at`,默认给你的是多表联合后的最右边的表的`created_at`,所以要使用`select slot_renewal_record`
```sql
select slot_renewal_record.* from slot_renewal_record
join slot slo on slo.id = slot_renewal_record.slot_id
join operator ope on slot_renewal_record.operator_id=ope.id where slot_renewal_record.park_id = 1 and slot_renewal_record.valid > 0 and slo.show_status = 1 and ope.name like "%luoqijun%" limit 0, 99;
```
# 24. 当写多表查询的后台逻辑
首先要在刚开始逻辑中做各种join，根据join完后的表格可以根据前端传进来的参数来做筛选出符合条件的结果，最后将前面得到的表格select("我们需要的实体类对应的表格.*"),通过分页函数拿到对应表格的实体类，再用拿到的实体类给我们的Model（要返回给前端的对象）层赋值。这样Model的内部结构和我们查询得到的实体类应该是差不多或者实体类拥有的属性包含了Model类的所有属性。
> 那么如果我们的Model需要的参数实体类中没有而在另外一个表格中，怎么办呢？
此时我们直接根据实体类`targetEntiy`拿到另外一个表格的实体类`otherEntiy`（target.id=other.id），然后用`otrherEntiy`给我们的Model赋值。
# 25. 当idea报错显示...is not an enclosing class
public class A {
public class B {

}
};

需要实例B类时,按照正逻辑是,A.B ab = new A.B();
那么编译器就会出现一个错误–“is not an enclosing class”
再翻看相关的java代码,发现原来写法出错了!正确的做法是
A a = new A();
A.B ab = a.new B();
或者
new A().new B();

没有静态(static)的类中类不能使用外部类进行.操作,必须用实例来进行实例化类中类.

# 26. java调用外部接口
```java
            //调用接口获取对应车牌的停车费
            HttpClient client=new HttpClient();
            JSONObject param=new JSONObject();
            param.put("uuid",uuid);
            param.put("parkId","2233");
            param.put("plateNo",plate);
            param.put("withoutSign",1);
            //获取接口返回结果
            String res="";
            try {
                res = client.post("http://www.4-xiang.com:4081/api/v2/thirdpart/maoku/lookup_fee",
                        param.toString(),
                        ContentType.APPLICATION_JSON.getMimeType());
            }catch (Exception e){
                logger.info("{}停车费用查询失败:{}",plate,e);
            }
            if(client.getLastStatusCode()=="200"){
                //do sth
            }
```
使用`HttpClient`对象发起`post`请求，url为文档给出的调用接口，第二个参数为json格式的字符串，第三个参数为`ContentType`,表示客户端传给服务器的文本类型，该接口返回的结果用res接收
# 27. String转为alibaba.JSONObject
`JSONObject resJSON= JSON.parseObject(res);`,当然res首先得是json格式的字符串,否则转换报错
# 28. 当我们将String类型转换为Number类型的时候
我们可以采用`Number.parseNumber()`方法，此处的Number代指Integer，Floate，Double等类型，我们可以使用`Double d=Double.parseDouble("500.55")`来将字符串类型转换Double类型
# 29. 使用String.format()
- 保留一位小数 `String.format("%.1f",33.333333)`
- printf（"%05d",1）输出：00001--->%0nd 用得比较多，表示输出的整型宽度至少为n位，不足n位用0填充
- printf（"%5d",1）输出：****1（*为空格）--->%nd 输出的整型宽度至少为n位，不足n位用空格代替
# 30 增加分页逻辑
```java
        Query query = db.from(MixcPayRecord.class).where("member_uuid",uuid).where("licence_plate",plate).orderBy("created_at desc");
        Pagination<MixcPayRecord> pagination = query.paginate(MixcPayRecord.class,page,10);
        int total=pagination.getTotal();
        List<MixcPayRecord> payRecordList = pagination.getData();
```

1. 不采用分页
我们通过
```java
List<MixcPayRecord> payRecordList = db.from(MixcPayRecord.class).where("member_uuid",uuid).where("licence_plate",plate).orderBy("created_at desc").all((MixcPayRecord.class);
```
便可以获取到符合查询条件的所有对象的一个list,这样可以一次性返回给前端，但是对服务器的压力比较大，故可以采用分页的形式
2. 采用分页的
```java
        Query query = db.from(MixcPayRecord.class).where("member_uuid",uuid).where("licence_plate",plate).orderBy("created_at desc");
        Pagination<MixcPayRecord> pagination = query.paginate(MixcPayRecord.class,page,10);
        int total=pagination.getTotal();
        List<MixcPayRecord> payRecordList = pagination.getData();
```
首先获得要查询结果的所有Query对象，然后调用对象的paginate()方法，把要返回的对象类型的class，要查询的页数，一页返回来的对象的个数封装到一个pagination对象里，然后使用pagination.getData()获取到所有的对象类型，当然，还要给前端传递一个对象的总个数
以方便做分页
## 31. 计算接口的耗时的时候
很明显在进入接口的时候使用系统函数获取当前时间t1，在接口快结束的地方再调用一次系统函数获取当前系统时间t2,然后接口耗时即为t2-t1
```java
Long startTs = System.currentTimeMillis();
Long endTs = System.currentTimeMillis();
Long delay=endTs-startTs;
```
 32. 常用查看日志的命令
1. `tail -f app.log`:默认查看最新10条日志记录并实时刷新
2. `tail -n 100 app.log`:查看最后100行数据
3. `tail -n -100 app.log`:查看从第100行开始到最后一行的数据
4. `tail -f app.log|grep --color -i 云QQ2020`:查看关键字“云QQ2020”并以颜色标注关键字
5. `tail -f app.log|grep -5 --color -i 云QQ2020`:查看关键字“云QQ2020”上下五行的数据并以颜色标注关键字

# 33. git clone工程的如何从master分支切换到dev分支
1. `git branch -D dev`
2. `git checkout -b dev origin/dev`

# 34. 字符串的转义和字符串的格式化
- 字符串转义：(侧重于在字符串中显示特殊字符)我们输出的字符串中可能包含很多不可见的ASCⅡ码或者特殊的符号(字符串里包含"")，我们只能使用类似"    /n       "来表示换行或者"    /"  /"      "来使得字符串输出时仍然含有""
- 字符串格式化：(侧重于将输出字符串的内容按一定的格式输出)我们如果想要将字符串中的某些变量按照一定的格式输出,可以使用String.format(String str,Object args...),这个format函数内中又有`转换符`和`转换符号标志`这两个概念，详情点[这里](https://segmentfault.com/a/1190000019350486)

# 35 关于方法中 public <T> List<T> getList(T t){}
第一种：
```java
public <T> List<T> getList(T t){}
```
第二种：
```java
public List<T> getList(T t){}
```
第一种写法和第二种写法在功能上是一样的，当我们采用第二种写法的时候，jvm在碰到`<T>`时候并不认识`<T>`,所以采用要在使用前声明一下告诉jvm`<T>`是什么，便有了第一种写法
> 第一种写法是正确的，第二种写法是不正确的
# 36 API与SDK
- API:前端调用后端数据的一个通道，就是我们俗说的接口，通过这个通道，可以访问到后端的数据，但是又无需调用源代码。

- SDK:工程师为辅助开发某类软件的相关文档、范例和工具的集合，使用SDK可以提高开发效率，更简单的接入某个功能。
（一个项目(app,web...)的半成品）
举例说明：一个产品想实现某个功能，可以找到相关的SDK，工程师直接接入SDK，就不用再重新开发了。
# 37 API(Application Programming Interface)与SPI(Service Provider Interface)
- API:大多数情况下，都是实现方来制定接口并完成对接口的不同实现，调用方仅仅依赖却无权选择不同实现。
- SPI:而如果是调用方来制定接口，实现方来针对接口来实现不同的实现。调用方来选择自己需要的实现方 
- 我的理解就是SPI:是支付宝制定下来一系列操作流程及其对应的接口，我们对其接口进行调用对接，我们在打通这么多接口后，支付宝会获取我们从打通的接口中传递的信息，支付宝会利用有用的信息，将用户的支付url指向我们通过接口向支付宝传递的我们自己的支付url
# 38 回调函数
你调用了系统实现(或者别人)的某个函数（比如 win32 API），而这个函数内又会调用一个由你实现的另一个函数，那么这个另一个函数就是所谓的回调函数。所以，一般来说，你只是不直接去调用罢了。所以，其实这个函数和别的函数，从函数的角度没有区别，只是人们名之回调函数。
## bin目录和lib目录
`bin`是指二进制binary的意思，是用来存放编译好的二进制文件，`lib`是存放函数库文件的文件夹
# mysql
## distinct
在使用distinct的时候有两种情况
- distinct 字段1：只针对字段一重复的内容进行去重
- distinct 字段1，字段2，字段3...：将所有的字段拼接成一个长的“字段”，如果这个“长字段”存在重复的情况则去重，否则不能去重

<font color=red>如果我现在必须要select一堆字段但是又想只是针对一个字段去重该怎么办呢？</font>

首先我们采用常规的方法`select distinct 字段1 from table1`但是此时不满足我们要`select 字段1,字段2,字段3 from table1`的要求，此时`distinct`是不符合要求的。我们可以使用`group by`来进行去重。---`select 字段1,字段2,字段3 from table1 group by 字段4`当然此处也可以使用字段1
## mysqld命令和mysql命令的关系
首先mysql启动的是一个可以执行sql语句的客户端，而mysql客户端需要连接到mysql服务，即为mysql客户端想要运行必须启动mysql服务，二启动mysql服务的命令就是`myslqd`----mysql daemon(精灵)
## mysql中timestamp和datastamp的区别
- datatime存储时间的时候不做任何改变直接存储，而timestamp存储的时候会先转换为世界时间然后存储，同样的timestamp取出来的时候做反向转换
- 初始化和自动更新
- - 自动更新：timestamp在修改其他列的时候此字段会自动的进行更新不需要手动的维护，而datatime不会自动的更新。
- - 初始化：如果没有对该字段进行赋值则自动的存储为当前的时间。
> 这就是为什么表中涉及到created_at时采用datatime（不做更新）而update_at时则使用timestamp（修改表中一个字段也需要自动更新，而timestamp可以做到自动更新）

## 
# 踩坑：boolean转int类型
```java
    boolean ? 1 : 0;
```
不知道为什么mac上跑没有问题但是阿里云上出现问题，没有条件去逐步测试，所以改成
```java
if(true)
{
    flag = 1;
}else{
    flag = 0;
}
```

# python
1. 如何指定Python代码按照utf-8格式
在头文件处加上
```python
# -*- coding: utf-8 -*-
```
# 杂项
## 关于支付宝alipay.trade.create(统一收单交易创建接口) 中传入三个必选参数仍然返回参数无效的解决办法
问题出在支付宝文档里的`user_id`选项为<font color=red>特殊可选</font>，但是这并不是可选参数，而是一个<font color=red>必选参数
</font>,那么如何获取这个参数呢？通过获取用户权限接口来使支付宝回调我们配置好的url，然后我们就可以从url中获取到信息了

## 微信车主服务对接
### 1. 调用接口报错"400 Bad Request"
问题是出在调用HttpClient的post方法的时候虽然传入了参数，但是忘记传入`Charsets.UTF-8`这个参数，导致解析xml出错
### 2. 传入的参数是xml格式
直接当做post的请求体，像是String一样，直接传入就行，微信内部自己解析