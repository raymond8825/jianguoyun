# 1. Web开发常用名词
# 1.1 web应用服务器
供向外部发布web资源的服务器软件（服务器=电脑硬件+服务器软件）

mysql+电脑硬件=数据库服务器

Tomcat+电脑硬件=web服务器
# 1.2 web资源
有很多的资源都可以是web资源，只要你放在web应用服务器中

1）静态资源：指web页面中供人们浏览的数据始终是不变。比如：HTML、CSS、	JS、图片、多媒体。

2）动态资源：指web页面中供人们浏览的数据是由程序产生的，不同时间点访问	web页面看到的内容各不相同。比如：JSP/Servlet、ASP、PHP

# 2. Hello Tomcat
Tomcat是中小型免费的web服务器，支持Java EE的servlet和jsp规范。（什么是规范？Java EE有13种规范，常用的这两种，其他不常用，自己百度）

不使用tomcat也可以打开html页面，但是可以在浏览器的地址里看到 `file:d:/test.html` 这样的格式，是通过打开本地文件的形式打开的

但是我们平时上网看到的html网址一般都是:
http://12306.com/index.html 这样的形式
这是因为有web服务器的存在
# 2.1 Tomcat文件目录
- webapps：是放web应用发布的目录
- conf：配置文件夹
- bin:文件夹存放着启动Tomcat服务的startup.bat文件

# 2.2 Tomcat中的web应用目录结构
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191029193700.png)

但是不同的tomcat中不一定都是含有web.xml,其中WEB-INF是受保护的目录，外界不能直接访问，因为里面的内容对于用户来说没用，而且一旦暴露会很危险。

这样手动创建出来的文件是可以发布的，但是我们平时会使用ide来创建工程，上述的文件结构已经自动帮我们给创建好了。![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191029214922.png)


# 2.3 eclipse绑定Tomcat
去Windows-->properties-->server-->tomcat,然后在Servers栏（和console在一起）里面双击服务器开始配置文件，server location选择第二个，deploy改为webapps
# 2.4 eclipse发布工程
直接选择run on server即可完成运行和发布工作

其实eclipse中的工程中所有文件夹只有WEBContent中的内容会发布（复制）到Tomcat中的webapps中，其他的文件并不会发不过去 