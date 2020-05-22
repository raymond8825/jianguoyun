# 1 JDBC和Java的关系
JDBC (Java DataBase Connection) 是通过JAVA访问数据库
# 2 Hello JDBC
## 2.1 为项目导入mysql-jdbc的jar包
### 2.1.1 注册驱动
1. 为项目导入mysql-jdbc的jar包
### 2.1.2 初始化驱动

`Class.forName("com.mysql.jdbc.Driver");`

1. 建立数据库连接

建立与数据库的Connection连接

这里需要提供：

数据库所处于的ip:127.0.0.1 (本机)

数据库的端口号： 3306 （mysql专用端口号）

数据库名称 how2java

编码方式 UTF-8

账号 root

密码 admin

### 2.1.3 获得语句执行者statement

Statement是用于执行SQL语句的，比如增加，删除
### 2.1.4 执行sql语句

s.execute执行sql语句

### 2.1.5 处理结果
### 2.1.6 释放资源

数据库的连接是有限资源，相关操作结束后，养成关闭数据库的好习惯
先关闭Statement
后关闭Connection


### 2.1.6 总结
可以用文件流的方式来回收Connetion和Statement对象资源
```java
package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;


public class testJDBC {
    public static void main(String[] args) {
    	//1. mysql驱动初始化
    	try 
    	{
    		Class.forName("com.mysql.jdbc.Driver");
    	}catch(ClassNotFoundException e)
    	{
    		e.printStackTrace();
    	}
    	
    	try (//这里的小括号写法时自动关闭资源对象c和s
    		//2 .建立数据库连接
    		Connection c=DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/how2java?characterEncoding=UTF-8","root","admin");
    		
    		//3. 创建执行对象statement
    		Statement s=c.createStatement();
    	)
        {
            String sql = "insert into hero values(null,\"诡雷\",100,29)";
            // 执行sql
            s.execute(sql);
              
        }catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
```
# 3 JDBC的增删改查crud
C 增加(Create)
R 读取查询(Retrieve)
U 更新(Update)
D 删除(Delete)

在JDBC中增加，删除，修改的操作都很类似，只是传递不同的SQL语句就行了。

查询因为要返回数据，所以和上面的不一样，将在下一章节讲解。

# 4 JDBC的查询
## 4.1 查询语句
executeQuery 执行SQL查询语句，返回值为ResulteSet对象，该对象有getInt方法，getString方法等，参数既可以传递第n列的数字n，也可以使用给出第n列的字段名字
```java
package curdofJDBC;

import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class curdofJDBC {
	public static void main(String[] args) {
		//进行数据库查询
		//1.mysql驱动初始化
		try {
			Class.forName("com.mysql.jdbc.Driver");
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}
		try//小括号中的是占用资源的对象，程序会自动释放资源
		(
				//2.建立数据库连接
				Connection c=DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/how2java?characterEncoding=utf-8","root","admin");
				//Connection c=DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/how2java?characterEncoding=UTF-8","root","admin");
				//3.创建执行sql的对象statement
				Statement s=c.createStatement();
		)
		{
//			String sql ="insert into hero values(null,\"耶格\",100,41)";
//			s.execute(sql);
			
			String sql="select * from hero";//查询hero表
			ResultSet rs=s.executeQuery(sql);//将查询返回结果保存至re对象中
			while(rs.next())//迭代器
			{
				int id=rs.getInt("id");
				String name=rs.getString("name");
				float hp=rs.getFloat("hp");
				int damage=rs.getInt("damage");
				System.out.printf("%d\t%s\t%f\t%d\t\n",id,name,hp,damage);
			}
		}catch(SQLException e)
		{
			e.printStackTrace();
		}
		System.out.println("sucessfully!");
	}

}

```

```sql
create table user(
    id int primary key,
    name varchar(10),
    password varchar(10)
);

```

## 4.2 SQL语句判断账号密码是否正确
判断账号密码的正确方式是根据账号和密码到表中去找数据，如果有数据，就表明密码正确了，如果没数据，就表明密码错误。

不恰当的方式 是把uers表的数据全部查到内存中，挨个进行比较。 如果users表里有100万条数据呢？ 内存都不够用的。
```java
package curdofJDBC;


import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.Statement;

import javax.lang.model.element.VariableElement;

import java.sql.ResultSet;
import java.sql.SQLException;

public class testJBDC {

	public static void main(String[] args) {
		
		//1. 初始化mysql驱动
		try {
			Class.forName("com.mysql.jdbc.Driver");
		}catch(ClassNotFoundException e){
			e.printStackTrace();
		}
		
		try
		(		//2. 与数据库建立连接
				Connection c=DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/how2java?characterEncoding=utf-8","root","admin");
				//3. 创建执行sql语句的对象
				Statement s=c.createStatement();
		)
		{
//			String sql="insert into user values(null,'dashen','thisispassword');";
//			s.execute(sql);
            String name = "dashen";
            String password = "thisispassword";
            
            String sql="select * from user where name=\""+name+"\" and password=\""+password+"\"";
//            System.out.println(sql);
            ResultSet rs=s.executeQuery(sql);
            //boolean res=(rs != null);//这样是不行的，必须用下面的re.next()运行一次
            boolean res=rs.next();
            if (res)
            {
            	System.out.println(rs.getString("name"));
            }
            else {
				System.out.println("用户名或者密码不正确");
			}
		}catch (SQLException e) {
			e.printStackTrace();
		}
	}

}

```
> 得到查询结果后一定要用rs.next()方法运行一下，至于为什么不清楚

# 5 在JDBC中使用预编译STATEMENT 以及它的优点
## 5.1 使用PreparedStatement
和 Statement一样，PreparedStatement也是用来执行sql语句的
与创建Statement不同的是，需要根据sql语句创建PreparedStatement
除此之外，还能够通过设置参数，指定相应的值，而不是Statement那样使用字符串拼接
## 5.2 PreparedStatement的优点1-参数设置
Statement 需要进行字符串拼接，可读性和维护性比较差
 
String sql = "insert into hero values(null,"+"'提莫'"+","+313.0f+","+50+")";
 

PreparedStatement 使用参数设置，可读性好，不易犯错
 
String sql = "insert into hero values(null,?,?,?)";
 ## 5.3 PreparedStatement的优点2-性能表现
 PreparedStatement有预编译机制，性能比Statement更快

Statement执行10次，需要10次把SQL语句传输到数据库端，数据库要对每一次来的SQL语句进行编译处理

PreparedStatement 执行10次，只需要1次把SQL语句传输到数据库端，数据库对带?的SQL进行预编译

 每次执行，只需要传输参数到数据库端
1. 网络传输量比Statement更小
2. 数据库不需要再进行编译，响应更快

## 5.4 PreparedStatement的优点3-防止SQL注入式攻击
用户在注册信息的时候，故意再注册信息中使用sql语句，而直接使用Statement会执行字符串拼接的sql语句，可能导致数据库运行不稳定。

假设name是用户提交来的数据
 
String name = "'盖伦' OR 1=1";
 

使用Statement就需要进行字符串拼接
拼接出来的语句是：
 
select * from hero where name = '盖伦' OR 1=1
 

因为有OR 1=1，这是恒成立的
那么就会把所有的英雄都查出来，而不只是盖伦
如果Hero表里的数据是海量的，比如几百万条，把这个表里的数据全部查出来
会让数据库负载变高，CPU100%，内存消耗光，响应变得极其缓慢

而PreparedStatement使用的是参数设置，就不会有这个问题

# 6 EXECUTE与EXECUTEUPDATE的区别
不同1：
execute可以执行查询语句
然后通过getResultSet，把结果集取出来
executeUpdate不能执行查询语句

不同2:
execute返回boolean类型，true表示执行的是查询语句，false表示执行的是insert,delete,update等等
executeUpdate返回的是int，表示有多少条数据受到了影响

相同点：
execute与executeUpdate的相同点：都可以执行增加，删除，修改
# 7 获取JDBC的元数据信息（即为有关数据库的信息）
# 8 如何在JDBC中使用事务
事务特点：在事务中的多个操作，要么都成功，要么都失败（加入不用事物，第一条SQL语句执行了，但是第二条SQL语句有错误，会导致数据错误，比如去银行，取走100，存进去200，第一条sql执行成功，但是第二条执行错误，就会导致数据不正确，所以事物的特点就很重要）
```java
//网站上有示例，每一个小的知识点都有示例
```
# 9 使用JDBC做一个ORM例子
ORM=Object Relationship Database Mapping

对象和关系数据库的映射

就是根据如何使用java程序与sql中数据交互

对象和关系数据库的映射

简单说，一个对象，对应数据库里的一条记录
# 10 基于JDBC设计DAO的实例
DAO=DataAccess Object

数据访问对象

实际上就是运用了练习-ORM中的思路，把数据库相关的操作都封装在这个类里面，其他地方看不到JDBC的代码

# 11 线程池
与线程池类似的，数据库也有一个数据库连接池。 不过他们的实现思路是不一样的。