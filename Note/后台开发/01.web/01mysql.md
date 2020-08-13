# 1.sql基础
sql是操作所有的关系型数据库的语言

- 数据行(记录)
- 数据列(字段)
- 数据表(数据行的集合)
- 数据库(数据表的集合)

对于web程序员来讲，重点是数据的crud（增删改查），必须熟练编写DQL、DML，能够编写DDL完成数据库、表的操作，其它语言如TPL、DCL、CCL了解即可

SQL语句主要分为：
- DQL：数据查询语言，用于对数据进行查询，如select
- DML：数据操作语言，对数据进行增加、修改、删除，如insert、udpate、delete
- TPL：事务处理语言，对事务进行处理，包括begin transaction、commit、rollback
- DCL：数据控制语言，进行授权与权限回收，如grant、revoke
- DDL：数据定义语言，进行数据库、表的管理等，如create、drop
- CCL：指针控制语言，通过控制指针完成表的操作，如declare cursor
## 1.2 主键
主键唯一可以确定一条记录且不使用任何业务相关的字段作为主键。（一般使用id作为主键）
身份证号、手机号、邮箱地址这些看上去可以唯一的字段，均不可用作主键。因为作为业务相关的字段，手机号可能变化，身份证号可能会变长，所以我们一般使用id作为主键
## 1.3 常见主键
1. 自增整数类型：数据库会在插入数据时自动为每一条记录分配一个自增整数，这样我们就完全不用担心主键重复，也不用自己预先生成主键；

2. 全局唯一GUID类型：使用一种全局唯一的字符串作为主键，类似8f55d96b-8acc-4636-8cb8-76bf8abc2f57。GUID算法通过网卡MAC地址、时间戳和随机数保证任意计算机在任意时间生成的字符串都是不同的，大部分编程语言都内置了GUID算法，可以自己预算出主键。

对于大部分应用来说，通常自增类型的主键就能满足需求。我们在students表中定义的主键也是BIGINT NOT NULL AUTO_INCREMENT类型。

# 2 mysql操作
查看当前已经选中的数据库使用`select database();`
## 2.1 登陆mysql
首先在服务中保证mysql服务为开启状态，使用`services.msc`打开服务或者在cmd管理员模式下使用`net start mysql`，然后登陆mysql，在cmd中输入`mysql -uroot -p密码`即可在cmd中使用MySQL
## 2.2 DDL数据定义语言
操作对象：数据库和表

关键字：`create`, `drop`, `alter`
### 2.2.1 DDL操作数据库
- 创建：`create database 数据库名称;`
- 删除：`drop database 数据库名称;`
- 常用命令：
- - 切换或者进入数据库：`use 数据库名称`
- - 查看所有数据库：`show databases;`
- - 查看当前数据库下的所有表：`show tables`
- - 查看表的结构：`desc 表名`
- - 查看建表语句（可以查看某个表在建表时使用的sql语句）：`show create table 表名`
- 当然也有修改数据库，但是只是修改数据库的名称，字符集，用不到，先不学

### 2.2.2 DDL操作表

- 创建表：`create table 表名(字段名称 字段类型 [约束 ],字段名称 字段类型 [约束 ]);`
- - 字段描述：`字段名称 字段类型 [约束 ]--->[]`表示可有可无
```sql
    create table person(
        id int primary key auto_increment,
        personname varchar(20)
    );
```
- 删除表：`drop table 表名;`
- 修改表:`alter table 表名 ...`
- - 修改表名：`alter table 旧表名 rename to 新表名;`
- - 添加字段：`alter table 表名 add 字段 字段描述;`
- - 修改字段名称：`alter table 表名 change 旧字段名称 新字段名称 新字段描述;`# 字段描述是必须的，否则报错
- - 修改字段描述：`alter table 表名 modify 字段名称 字段类型 [约束];`
- - 删除字段：`alter table 表名 drop 字段名字;`

## 2.3 DML数据操作语言
操作对象：记录（行）

关键词：insert update delete
### 2.3.1 DML操作记录（行）
- 插入：
- - 格式1：`insert into 表名 values(字段值1,字段值2,...);`*默认插入全部字段，即为必须保证values后面的字段的类型和顺序必须和表中的结构一致，如果是数字，可以不加引号，如果不是数字，要记得加上引号，单双引号都行*
- - 格式2：`insert into 表名 (字段名1,字段名2...) values(字段值1,字段值2...);`*插入指定字段，也可以插入全部字段，而且字段这里不用引号*
- 修改：`update 表名 set 字段名1=字段值1,字段名2=字段值2 [where 条件];`*如果不增加条件where，则默认对所有的记录的字段 *
- 删除：`delete from 表名 [where 条件];`

## 2.4 DQL数据查询语言
关键词：select
```sql
# 想练习查询，首先得建立数据库文件
create table products(
	pid int primary key auto_increment,
	pname varchar(20),
	price double,
     pnum int,
     cno int,
	pdate timestamp
);

insert into products values (null,'泰国大榴莲',98,12,1,null);
insert into products values (null,'新疆大枣',38,123,1,null);
insert into products values (null,'新疆切糕',68,50,2,null);
insert into products values (null,'十三香',10,200,3,null);
insert into products values (null,'老干妈',20,180,3,null);
insert into products values (null,'豌豆黄',20,120,2,null);

```
> 1. 基础查询
- `select ... from 表名 where 条件 group by 分组字段 having 条件 order by 排序字段 asc（升序）|desc（降序）;`
- 查询指定字段：`select 字段名1，字段名2 from 表名;`
- 去重查询：`select distinct 字段名1,字段名2 from 表名`*比如查询所有人的年龄字段，但是显示出重复的年龄值，但是我们却不想看到重复的年龄值*
- 查询结果之上进行运算，但是数据库的值不受影响：`select price+10 from prodects;`*比如将所有的商品的价格加10元显示，数据库不受影响*
- 给查询结果起新的名字：`select price+10 [as] 别名 from products;`*刚才在运算结果上计算，但是却不知道什么意思，就可用新的名字来提示*
> 2. 条件查询
- 比如查询商品名称为十三香的商品的所有信息：`select * from products where pname="十三香";`
- 查询商品价格>60元的所有的商品信息：`select * from products where price>69;`
- 查询价格为38，68，98的商品信息：`select * from products where price in(38,68,98);`或者`select * from products where price =38 or price=68 or price=98;`
- 查询所有商品中包含”新”的商品（模糊匹配）：`字段名 like "匹配规则";`
- - 匹配内容：%表示任意字符
- - - "新"--->值为"新"
- - - "%新"--->值以"新"结尾
- - - "新%"--->值以"新"开头
- - - "%新%"--->值中包含"新"
- - 匹配个数：`__`两个`_`表示占据两个字符位置

where后的条件写法：

    * > ,<,=,>=,<=,<>
    * like 使用占位符 _ 和 %  _代表一个字符 %代表任意个字符. 
        * select * from product where pname like '%新%';
    * in在某个范围中获得值.
        * select * from product where pid in (2,5,8);

> 3. 高级查询
1. 排序查询
- 查询所有商品，按价格进行排序（asc-升序，desc-降序）：`select * from products order by price desc;`
- 查询名称有”新“的商品信息并且按照价格降序排列：`select * from products where pname like "%新%" order by price desc;`
2. 聚合函数：（之前得到的结果都是以行为结果，聚合函数是以列为结果，个数为一个，而且会忽略null值）`sum(),avg(),max(),min(),count()`
- 获得所有商品的价格总和：`select sum(price) from products;`
- 获得商品中的价格平均数：`select round(avg(price),2) from products;`#round是保留avg(price)两位小数
- 获得商品表中有多少条记录：`select count(*) from products;`

3. 分组：使用group by，位于where后面order前面,分组往往伴随着聚合函数
> 当后面一旦出现了`group by`,那么此时sql语句中的聚合函数都是对于当前分组的统计（group by就好像是把大表按分组分成了几个小表格，然后select的字段都是针对分好组的小表格，得到的数据也分别对应小表格）
- 根据con字段分组，然后统计每组商品的种类数量：`select cno,count(*) from products group by cno;`
- 根据cno分组，然后统计每组商品的总数量，并且总数量>200：`select cno,sum(pnum) from products group by cno having sum(pnum)>200;`

where和having的区别：
- where是对分组前的数据进行过滤且后面不能跟聚合函数
- having是对分组后的数据（要放在group by后面）进行过滤且后面可以跟上聚合函数

> 4. 数据类型（了解）

|java|mysql|
|-|-|
|byte|tinyint|
|short|smallint|
|int|int★|
|long|bigint|
|char|varchar(n)/char(n),varchar是可变长度，最长为n,char为固定长度，始终长度为n|
|string|varchar(n)/char(n)★,varchar是可变长度，最长为n,仅mysql中有，char为固定长度，始终长度为n|
|boolean|tinyint/int代替|
|float|float|
|double|double|
|java.sql.Date|date|
|java.sql.Time|time|
|java.sql.Timestamp|timestamp★（时间戳，如果值为null，默认使用当前系统时间存入数据库中）|
||datetime★（日期加时间）|
|java.sql.Clob(长文本)|text（仅mysql中有）|
|java.sql.Blob(大文件二进制)|blob|
> 5. 约束

作用：为了保证数据的完整性和有效性。

mysql常见约束有四种：primary key(主键约束),unique(唯一约束),not null(非空约束),foreign key(外键约束)

1. 主键约束：被修饰过的字段唯一非空（一张表只有一个主键，一个主键可以包含多个字段）

主键的三种使用方式：
- 创建表的时候添加约束：`字段名称 字段类型 primary key`
- 建表的同时在约束区域添加约束，所有的字段在声名完成后，就是约束区域了，注意是在所有的字段声名完成后：
```sql
create table test(
    ...
    primary key(字段1,字段2)
    );
```
- 建表完成后，通过修改表的结构添加约束：`alter table 表名 add primary key(字段名1,字段名2...);`

1. 唯一约束（了解，因为可以通过java来完成，而不是sql）：
被装饰过的字段唯一，但是可以有多个null，而且可以有的多个字段为null

唯一约束的常见方式：和主键约束，一模一样

3. 非空约束（了解）

特点：被修饰的字段非空

创建方式：和主键约束的第一种一样，且只有一种创建方式

4. 外键约束()
下面有讲具体实例。


# 3. 创建多表，可以描述表与表之间的关系

需求：把网上商城里面的实体创建成表，并且将他们之间建立关系。

技术分析：网上商城实体：用户 订单 商品 分类

ER图可以描述实体与实体之间的关系：实体用矩形来表示，属性用椭圆来表示，关系用菱形来表示，但是在数据库中应该怎么表示呢？
## 3.1 一对多

> 开发中，
>
> - 一对多关系，其中一方称之为主表或者表，多方称之为从表或者多表。为了表示一对多的关系，一般会在多表的添加一个字段，字段名称自定义为（建议：主表名称_id）字段类型一般和<font color="red">主表的主键字段类型</font>保持一致，我们称这个字段为外键。

用户和订单
```sql
 # 创建用户表
create table user(
    id int primary key auto_increment,
    username varchar(20)
);
```
```sql
 # 创建订单表
create table ordergoods(
    orderid int primary key auto_increment,
    totalprice double,
    user_id int 
);
```
```sql
# 添加用户数据
insert into user values(3,"zhangsan");
insert into user values(4,"lisi");
insert into user values(5,"wangwu");
# 添加订单数据
insert into ordergoods values(1,1314,3);
insert into ordergoods values(2,1314,3);
insert into ordergoods values(3,1314,4);
```

数据写入完成后，如果一不小心将用户表中的李四删除，就会发现订单表中的李四的订单就找不到主人了，就变成了垃圾数据，所以我们需要解决这个问题

解决：为了保证数据的有效性和完整性，添加约束（外键约束），在多表的一方，添加外键约束`alter table 多表名称 add foreign key(外键名称) references 一表名称(主键);`，对于本例来说`alter table ordergoods add foreign key(user_id) references user(id);`(这样可以是因为表ordergoods建表的时候已经有了user_id字段,如果没有该字段,此种增加外键的方式会提示缺少该字段)

添加了外键约束后有以下特点★：
1. 主表中不能删除从表中已经引用的数据
2. 从表中不能添加主表中不存在数据

> ★一对多问题的总结：在多表中添加一个外键，名称一般为主表的名称_id，字段类型一般和主表的主键类型保持一致，为了保证数据的有效性和完整性，多表的外键上添加外键约束即可。
## 3.2 多对多
订单和商品

> 在开发中，我们会引入一张中间表，在中间表中存放两张表格的<font color = "red">主键</font>，一般还会将这两个主键设置成中间表的联合主键。这样将一个多对多关系拆开成为两个一对多，根据一对多关系可以知道，为了保证数据的有效性和完整性，在中间表上添加两个外键约束即可。

```sql
# 创建商品表
create table product(
    id int primary key,
    name varchar(20),
    price double
);
```
```sql
# 创建中间表
create table orderitem(
    oid int,
    pid int
);
```
```sql
# 添加两个外键约束
alter table orderitem add foreign key(oid) references ordergoods(orderid);
alter table orderitem add foreign key(pid) references product(id);
```
# 4 多表查询
技术分析：内连接★，外连接★，子查询★，这三个是建立在笛卡尔积的基础上
> 内外连接就是一个`join on`为重点，外连接是在内连接的基础上在`join`的左侧加上了`right`和`left`。<font color="red">内连接是求交集，外连接求并集</font>。子查询则是将()中的查询结果返回回来，当返回回来的是一个值的时候用=，当返回回来的是多值（表）的时候，就用in
1. 内连接:

显示内连接(★)：`select a.*,b.* from a [inner] join b on ab表的连接条件;`

隐式内连接（不掌握）：`select a.*,b.* from a,b where ab的连接条件`

```sql
-- 用户表(user) 
   create table user (                                  
          id int auto_increment primary key,                
          username varchar(50)  -- 用户姓名                                                
        );

-- 订单表(orders)
   create table orders (                                                  
          id int  auto_increment primary key,                                  
          price double,                                           
          user_id int                                       
        );
-- 给订单表添加外键约束
alter table orders add constraint user_fk foreign key (user_id) references user(id); 

-- 向user表中添加数据
		insert into user values(3,'zs');
		insert into user values(4,'ls');
		insert into user values(5,'ww');
		insert into user values(6,'zl');

-- 向orders 表中插入数据
		insert into orders values(1,1314,3);
		insert into orders values(2,1314,3);
		insert into orders values(3,15,4);
		insert into orders values(4,315,5);
		insert into orders values(5,1014,null);
```
问题一：查询用户订单，没有订单的用户不显示

隐式内连接：`select user.*,orders.* from user,orders where user.id=orders.user_id;`

显式内连接(掌握)：` select user.*,orders.* from user inner join orders on user.id=orders.user_id;` 

2. 外连接

左外连接（★）：`select a.*,b.* from a left [outer] join b on 连接条件;`--->先展示join左边的(a)表的所有数据，根据条件关联查询join右边的表(b),符合条件则展示，不符合以null显示。即为不像内连接只查询多表之间“交集”，而是多表的“并集”,（外连接包含了内连接）

右外连接：`select a.*,b.* from b right [outer] join a on 连接条件;`--->先展示join右边的(a)表的所有数据，根据条件关联查询join左边的表(b),符合条件则展示，不符合以null显示

问题二：查询所有用户的订单详情(用左外连接)

首先确定哪个表在左边--->user，因为分析的是所有用户
`select user.*,orders.* from user left join orders on user.id=orders.user_id;`

问题三：查询所有订单的用户详情（用右外连接）

首先分析那张表在右侧--->如果用右外连接，则先展示join右侧的表，而这张表应该是所有订单的表，所以join右侧的表是orders
`select orders.*,user.* from user right join orders on user.id=orders.user_id;`# select后面的字段顺序决定了表格列的排列顺序。

3. 子查询（★）

一个查询依赖于另一个查询。

问题一：查询用户为张三的订单详情（如果返回的查询结果只有一个值，那我们用=号）

问题想知道的是订单信息，首先可以想到`select * from orders where username="张三"`但是`from orders`中并没有`username`字段，但是有`user_id`作为外键，因此我们需要在`user`表中找到姓名为张三的`id`,所以
```sql
select id from user where username="张三";
select * from orders where user_id = 3;
```
但是这样很繁琐，要单独写两个sql句子，多以要合二为一

```sql
select * from orders where user_id = (select id from user where username="张三"); 
```

也可以用内连接实现`select orders.* from orders,user where orders.user_id = user.id and user.username="张三";`

问题二：查询单个订单价格大于三百的所有用户信息（如果返回的结果为多行一列的情况，我们用in）

分析：想要的是用户信息，首先可以想到

`select * from user where id =?;`

接下来找出所有的订单价格大于三百的`user_id`

`select user_id from orders where price>300;`

综合可得

`select * from user where id in (select user_id from orders where price>300);`

问题三：查询订单价格大于300的所有用户的id（如果返回的结果为多行多列，将返回的结果作为临时表存在）

内连接：`select user.id from user join orders on user.id=orders.user_id and orders.price>300;`

子查询：`select user.*,tmp.* from user,(select * from orders where price>300) as tmp where user.id=tmp.user_id;`# 本质上还是内连接查询，而且这里用到了给列表起别名



> 补充知识：


1. truncate（清空表）：
`truncate 表名;`干掉表格，重新创建一张空表格

和delete from的区别

|truncatedelete from|truncate|
|-|-|
|逐条删除表中数据|直接删除整张表|
|删空表格后仍有表格的全局变量|整个表格都被删除，自然没有全局变量的说法|

2. auto_increment自增
  
   要求：
- 被修饰的字段类型首先要支持自增，一般都是整数
- 被修饰的字段必须是一个key，一般是primary key
3. 建表的时候使用的timestamp和datetime
--添加CreateTime 设置默认时间 CURRENT_TIMESTAMP 
ALTER TABLE `table_name`
ADD COLUMN  `CreateTime` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ;

 

--修改CreateTime 设置默认时间 CURRENT_TIMESTAMP 
ALTER TABLE `table_name`
MODIFY COLUMN  `CreateTime` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' ;

 

--添加UpdateTime 设置 默认时间 CURRENT_TIMESTAMP   设置更新时间为 ON UPDATE CURRENT_TIMESTAMP 
ALTER TABLE `table_name`
ADD COLUMN `UpdateTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间' ;

 

--修改 UpdateTime 设置 默认时间 CURRENT_TIMESTAMP   设置更新时间为 ON UPDATE CURRENT_TIMESTAMP 

ALTER TABLE `table_name`
MODIFY COLUMN `UpdateTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间' ;