# 1. servlet
什么是servlet？

- init方法并不是服务器启动时运行，而是第一次HTTP请求时运行init方法（但是这取决于配置文件，当在web.xml---servlet---load-on-startup标签中随便设置一个值，该值代表优先级，数字越小级别越高）
# 2. 自定义模板
windows---preference--java---template

# 3. 关于导包（jar）
目前我只是知道要导入jar格式的包，eclipse中任何格式的文件都可以导入而且可以build path，但是不起作用，我们必须导入jar的包，但是jar中的是编译过后的.java格式的文件，后缀为.class并不是源码，所以我们不一定可以看到源码。

# 4.c3p0连接池
```java
ComboPooledDataSource c3p0DataSource=new ComboPooledDataSource();
```

# 5.spring
1. 导包
2. 创建对象
3. 然后是创建用于框架与框架之间交流的xml文件，建议放在src目录下，命名建议为applicationContext.xml，spring就是通过这个xml文件来创建对象。
4. 为创建的xml文件添加约束，很复杂，看视频
## 5.1 spring创建对象的三种方式
1. 无参创建对象（掌握）

```java
    	@Test
	public void fun1() {
		//1. 创建容器对象,其中xml文件的地址从只需要写入src文件夹后面的文件路径
		ApplicationContext ac = new ClassPathXmlApplicationContext("b_create/applicationContext.xml");
		//2.向容器中要user对象
		User u=(User)ac.getBean("user"); 
		//3.
		System.out.println(u);
		
	}
```
可以看到我们在外部提供了User类，然后直接向spring框架要user对象，而spring框架是如何知道的呢，是通过提供的xml文件。
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.springframework.org/schema/beans" xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.2.xsd ">
	<!-- 将User对象交给spring容器管理 -->
	<!-- Bean元素:使用该元素描述需要spring容器管理的对象
			class属性:被管理对象的完整类名.
			name属性:给被管理的对象起个名字.获得对象时根据该名称获得对象.  
					可以重复.可以使用特殊字符.
			id属性: 与name属性一模一样. 
					名称不可重复.不能使用特殊字符.
			结论: 尽量使用name属性.
	  -->
	<bean  name="user" class="bean.User" >
	</bean>
</beans>
```

xml中的bean中的name属性值是给spring中的参数传递参数，指定创建哪个类，然后class是指定创建那个类对象。

2. 静态工厂（了解）
3. 实例工厂（了解）















