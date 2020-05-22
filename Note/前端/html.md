# html学习
## html简介
什么是 HTML？
HTML 是用来描述网页的一种语言。

## HTML 文档 = 网页
- HTML 文档描述网页
- HTML 文档包含 HTML 标签和纯文本
- HTML 文档也被称为网页
- Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容：
```html
<html>
    <body>
        <h1>标题</h1>
        <p>段落</p>
    </body>
</html>
```
- `html` 与 `/html` 之间的文本描述网页
- `body` 与 `/body` 之间的文本是可见的页面内容
- `h1` 与 `/h1` 之间的文本被显示为标题
- `p` 与 `/p` 之间的文本被显示为段落
## html基础
- HTML 标题（Heading）是通过 `h1` - `h6` 等标签进行定义的。
- HTML 段落是通过 `p` 标签进行定义的。
- HTML 链接是通过 `a` 标签进行定义的。（其中需要在a标签的href属性中指定链接地址，属性将在之后学习）
- HTML 图像是通过 `img` 标签进行定义的。（图像的名称和尺寸是以属性的形式提供的）
## html元素
HTML 文档是由 HTML 元素定义的，HTML 元素指的是从开始标签（start tag）到结束标签（end tag）的所有代码。
> HTML 元素语法
- HTML 元素以开始标签起始
- HTML 元素以结束标签终止
- 元素的内容是开始标签与结束标签之间的内容
- 某些 HTML 元素具有空内容（empty content）
- 空元素在开始标签中进行关闭（以开始标签的结束而结束）
- 大多数 HTML 元素可拥有属性
> 嵌套的 HTML 元素
- 大多数 HTML 元素可以嵌套（可以包含其他 HTML 元素）。
> 空的html元素
- 没有内容的 HTML 元素被称为空元素。空元素是在开始标签中关闭的。`br` 就是没有关闭标签的空元素（`br/` 标签定义换行）。
## html属性
- 属性为html元素提供附加的信息
- 属性总是以名称/值对的形式出现，比如：name="value"。

- 属性总是在 HTML 元素的开始标签中规定。
### 始终为属性值加引号（是属性值，不是属性名）
属性值应该始终被包括在双引号内。在某些个别的情况下，比如属性值本身就含有双引号，那么您必须使用单引号
> html元素可用的属性有很多[html手册](https://www.w3school.com.cn/tags/index.asp)，有某些标签特有的，也有所有标签基本都有的属性[html标准属性参考手册](https://www.w3school.com.cn/tags/html_ref_standardattributes.asp)
## html标题
- 默认情况下，HTML 会自动地在块级元素前后添加一个额外的空行，比如段落、标题元素前后，所以浏览器会自动地在标题的前后添加空行。
- <hr /> 标签在 HTML 页面中创建水平线
### html注释
自己百度
## html段落
段落是通过 `p` 标签定义的。
> 浏览器会自动地在段落的前后添加空行。（`p` 是块级元素）提示：使用空的段落标记 `p` 和`/p` 去插入一个空行是个坏习惯。用 `br /` 标签代替它！所有连续的空格或空行都会被算作一个空格
## html样式
样式可以用css来完成，将在后来学习，现在学习html标签中的style属性。
```html
<html>

<body style="background-color:yellow">
<h2 style="background-color:red">This is a heading</h2>
<p style="background-color:green">This is a paragraph.</p>
</body>

</html>
```
```html
<html>

<body>
<h1 style="font-family:verdana">A heading</h1>
<p style="font-family:arial;color:red;font-size:20px;">A paragraph.</p>
</body>

</html>
```
## HTML 文本格式化
将文字以各种各样的格式输出到html页面上
[各种格式化标签和例子](https://www.w3school.com.cn/html/html_formatting.asp)
## html引用
| 标签         | 描述                             |
| ------------ | -------------------------------- |
| `abbr`       | 定义缩写或首字母缩略语。         |
| `address`    | 定义文档作者或拥有者的联系信息。 |
| `bdo`        | 定义文本方向。                   |
| `blockquote` | 定义从其他来源引用的节。         |
| `dfn`        | 定义项目或缩略词的定义。         |
| `q`          | 定义短的行内引用。               |
| `cite`       | 定义著作的标题。                 |
## html计算机代码标签
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20190924152036.png)
## html注释
< !-- 再次写入注释内容 -->（其中开头的!的前面不能有空格，如果有就会再html中就不会起作用，但是markdown默认执行html格式，所以这里的空格是故意破坏html格式）

在这里html注释有一个隐藏的用法
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20190924153013.png)
会发现< img>标签嵌套再注释标签中，但是实际中标签嵌套是不允许这样的，仔细观察发现，其实这个< img>就相当于注释标签的一段话
### 条件注释
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20190924153542.png)
## html css
> 通过html4.0可以将html代码中的格式代码都统统移出去html文档，然后移入一个独立的样式表

之前讲过想要改变一个标签的样式，可以在标签中使用style属性来完成，这在之前有介绍，比如
```html
<html>
    <head>
    </head>
    <body>
        <p style="background-color:blue">
        这是一个段落
        </p>
    </body>
</html>
```
现在可以有一个更好的方法来完成该项操作

```html
<html>
    <head>
        <style type="text/css">
        p {color:blue}
        </style>
    </head>
    <body>
        <p>
        这是一个段落
        </p>
    </body>
</html>
```
### 如何再html中使用css
1. 外部样式表（作用于多个html文件）
   
   该功能通过link标签来实现，该标签只能位于head标签中，但是可以重复多次出现，他是一个空元素，仅包含属性。
   当样式需要被应用到很多页面的时候，外部样式表将是理想的选择。使用外部样式表，你就可以通过更改一个文件来改变整个站点的外观。（一次写就可以再多个文件中进行外部引用，不用再逐个文件写样式了）
```html
    <head>
    <link rel="stylesheet" type="text/css" href="mystyle.css">
    </head>
```
2. 内部样式表(作用于单个html文件)
   
   当某个单独文件需要特别的样式的时候可以使用内部样式表，可以在该文件的head标签中通过< style>标签来定义内部样式表格
```html
   <head>
    <style type="text/css">
    body {background-color: red}
    p {margin-left: 20px}
    </style>
    </head>
```
3. 内联样式（作用于个别标签上）
   
    当特殊的样式需要应用到个别元素时，就可以使用内联样式。 使用内联样式的方法是在相关的标签中使用样式属性。样式属性可以包含任何 CSS 属性。以下实例显示出如何改变段落的颜色和左外边距。
```html
<p style="color: red; margin-left: 20px">
This is a paragraph
</p>
```
## html链接
我们使用a标签来再html中创建链接，其中有两种使用a标签的方式：
1. 通过href属性：创建指向另一个文档的链接
2. 通过使用name属性：创建文档内的书签

`<a href="http://www.baidu.com"> 链接文字 </a>`
"链接文字"不一定是文本，也可以其他的html元素--->图片

### name属性
用于快速定位页面，类似top等，用name属性来定义锚点，用href来定位到锚点处

`<a name="top">点击即可回到页首(往往这句话可以不写，这样锚点再html页面上就不会显示)</a>`

`<a href="#top">top(这里要在页面中显示，提醒用户从当前位置跳跃到页首)</a>`

### target属性
使用 Target 属性，你可以定义被链接的文档在何处（浏览器是否打开新的标签页）显示。
`<a href="http://www.baidu.com" target="_blank ">百度</a>`

## html图像
`<img>`是空标签，就是说只包含属性，没有闭合标签
### src属性
要想在html中显示图片，需要使用src属性，属性值为图像的url地址
`<img src="url" />`
### 替换文本属性alt
该属性作用是当图片无法加载时候，浏览器将显示这个文字来代替图像，告诉读者她所失去的信息
### align
用于控制文本对齐，在一句话中插入`img`标签，则图片会在一句话的中间，这就涉及到图片位于这一行的top，middle，bottom了，默认为botton，当然还有left和right，这两个决定了图片显示在一句话的左边还是右边
## 表格
表格由 `<table>` 标签来定义。每个表格均有若干行（由 `<tr>` 标签定义），每行被分割为若干单元格（由 `<td>` 标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。
## html块元素和内联元素
html中有很多元素（元素的定义之前有解释）这些元素又分为块元素和内联元素
### 块元素（block level element）
块级元素在浏览器显示时，通常会以新行来开始（和结束）。
例子：`<h1>, <p>, <ul>, <table>`
### 内联元素
内联元素在显示时通常不会以新行开始。
例子：`<b>, <td>, <a>, <img>`
#### div元素
div是块元素，它是可用于组合其他 HTML 元素的容器。该元素没有特殊的含义，但是由于他是块级别的元素，浏览器会在其前后显示空行*和css一起使用，div可以对大的内容块设置样式属性*

#### span元素
span是内联元素，可用用作文本的容器，span也没有特殊的含义，与css一同使用的时候，可以作为部分文本设置样式属性
## html类
> 虽然叫做html类，但是设置的类却是被html元素所应用的

对html文档设置类来分类，是我们能够对不同元素的类定义不同的css样式，为相同的类设置相同的样式

经过上面的学习，我们知道div可以将很多html元素包含到一个div块中来，div当然也属于html中的一个元素，那么我们就可以给div元素设置一个标签`<div class="nba_star">`
然后就可以在head标签中定义css样式，并且将css名字定义为".nbastar"，然后就可以在所有class属性为"nbastar"的div元素来应用该css格式
```html
<!DOCTYPE html>
<html>
<head>
<style>
.cities {
    background-color:black;
    color:white;
    margin:20px;
    padding:20px;
} 
</style>
</head>

<body>

<div class="cities">
<h2>London</h2>
<p>
London is the capital city of England. 
It is the most populous city in the United Kingdom, 
with a metropolitan area of over 13 million inhabitants.
</p>
</div> 

</body>
</html>
```
对于内联元素span也是，虽说是行内元素，但是也是一个html元素，那么他就可以设置class属性，也就可以应用css格式
```html
<!DOCTYPE html>
<html>
<head>
<style>
  span.red {color:red;}
</style>
</head>
<body>

<h1>My <span class="red">Important</span> Heading</h1>

</body>
</html>
```
## html布局
使用div来作为布局工具，轻松通过css对其进行定位。（这里的div用id属性来定位，属性值在css文件中设置，不知道是否可以用div的class属性来设置值<sup>?</sup>）
## RWD响应式web设计
- RWD 指的是响应式 Web 设计（Responsive Web Design）
- RWD 能够以可变尺寸传递网页
- RWD 对于平板和移动设备是必需的
## 使用Bootstrap
另一个创建响应式设计的方法，是使用现成的 CSS 框架。

Bootstrap 是最流行的开发响应式 web 的 HTML, CSS, 和 JS 框架。

Bootstrap 帮助您开发在任何尺寸都外观出众的站点：显示器、笔记本电脑、平板电脑或手机：
## html框架
通过使用框架，可以是浏览器窗口显示不止一个页面。每份HTML文档称为一个框架，并且每个框架都独立于其他的框架。
### 使用框架的缺点
- 开发人员必须跟踪更多的html文档
- 很难打印整张页面
### 框架结构标签`frameset`
- 框架结构标签`<frameset>`定义如何将窗口分割为框架
- 每个 frameset 定义了一系列行或列
- rows/columns 的值规定了每行或每列占据屏幕的面积
编者注：frameset 标签也被某些文章和书籍译为框架集。
```html
<frameset cols="25%,75%">
   <frame src="frame_a.htm">
   <frame src="frame_b.htm">
</frameset>
```
在上面这个例子中，我们设置了一个两列的框架集。第一列被设置为占据浏览器窗口的 25%。第二列被设置为占据浏览器窗口的 75%。HTML文档 "frame_a.htm" 被置于第一个列中，而 HTML文档 "frame_b.htm" 被置于第二个列中
> 假如一个框架有可见边框，用户可以拖动边框来改变它的大小。为了避免这种情况发生，可以在 <frame> 标签中加入：noresize="noresize"。
## html内联框架iframe标签
`<iframe src="https://www.baidu.com" height="200" width="200" frameborder="0">`
<!--<iframe src="http://www.365pcbuy.com/article-232.html" height="200" width="200" frameborder="0">-->

### iframe删除边框
frameborder 属性规定是否显示 iframe 周围的边框。

设置属性值为 "0" 就可以移除边框

### html背景
背景是在body中来配置，该标签拥有两个配置背景的属性：一个是bgcolor和backgroud
### bgcolor属性
将背景设置为某种颜色，属性值为十六进制，rgb，或者颜色的名字

### background属性

可以将背景设置为图像，属性值为图形的url（可以是相对地址或者绝对地址），如果图像尺寸小于浏览器窗口，那么图像将在浏览器上进行平铺

## html脚本

javascript使 HTML 页面具有更强的动态和交互性

### script标签

`<script>`签用于定义客户端脚本，比如 JavaScript。

script 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。

必需的 type 属性规定脚本的 MIME 类型。

JavaScript 最常用于图片操作、表单验证以及内容动态更新。

```html
<script type="text/javascript">
document.write("Hello World!")
</script>
```

### noscript标签

当浏览器不支持脚本的时候，noscript标签中的内容才会显示，相当于是一个提醒。

##  html文件路径

文件路径描述了网站文件夹结构中某个文件的位置。

文件路径会在链接外部文件时被用到：

- 网页
- 图像
- 样式表
- JavaScript

> 最好使用相对路径，这样就可以在各个电脑上运行

## html头部元素

### head标签

<head> 元素是所有头部元素的容器

以下标签都可以添加到 head 部分：`<title>、<base>、<link>、<meta>、<script> 以及 <style>。`
### title元素
`<title>` 标签定义文档的标题。

title 元素在所有 HTML/XHTML 文档中都是必需的。

title 元素能够：

- 定义浏览器工具栏中的标题
- 提供页面被添加到收藏夹时显示的标题
- 显示在搜索引擎结果中的页面标题
### base元素（不懂）
### link元素
常用于定义文档与外部资源(最常用于连接样式表)
```html
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css" />
</head>
```
### style元素
为html文件提供文档定义样式信息
### meta元素

元数据（metadata）是关于数据的信息。

`<meta>` 标签提供关于 HTML 文档的元数据。元数据不会显示在页面上，但是对于机器是可读的。

典型的情况是，meta 元素被用于规定页面的描述、关键词、文档的作者、最后修改时间以及其他元数据。

<meta> 标签始终位于 head 元素中。

元数据可用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他 web 服务。一些搜索引擎会利用 meta 元素的 name 和 content 属性来索引您的页面.

下面的 meta 元素定义页面的描述：
```html
<meta name="description" content="Free Web tutorials on HTML, CSS, XML" />
```
下面的 meta 元素定义页面的关键词：
```html
<meta name="keywords" content="HTML, CSS, XML" />
```
> name 和 content 属性的作用是描述页面的内容。
### script元素（已讲过）
## html字符实体
在 HTML 中，某些字符是预留的。

在 HTML 中不能使用小于号（<）和大于号（>），这是因为浏览器会误认为它们是标签。

如果希望正确地显示预留字符，我们必须在 HTML 源代码中使用字符实体（character entities）。
```html
<!DOCTYPE html>
<html>
<body>

<h2>字符实体</h2>

<p>&X;</p>
<p>&#174</p>
<p>&#pound</p>

<p>用实体数字（比如"#174"）或者实体名称（比如 "pound"）替代 "X"，然后查看结果。</p>

</body>
</html>
```
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20190926153356.png)
## html url
url:URL 的英文全称是 Uniform Resource Locator，中文也译为“统一资源定位符”。
[url的教程](https://www.w3school.com.cn/html/html_url.asp)
## URL 编码
url 只能使用 ASCII 字符集来通过因特网进行发送。

由于 URL 常常会包含 ASCII 集合之外的字符，URL 必须转换为有效的 ASCII 格式。

URL 编码使用 "%" 其后跟随两位的十六进制数来替换非 ASCII 字符。

URL 不能包含空格。URL 编码通常使用 + 来替换空格。
## html web服务器
## html文档类型
`<!DOCTYPE>` 声明帮助浏览器正确地显示网页。
# html xhtml
[之后再来学习xhtml](http://www.w3school.com.cn/html/index.asp)
# html表单
## html表单
HTML 表单用于搜集不同类型的用户输入。
### form元素
form元素定义html表单，form来表示一个html表单,而各种各样的表单元素则写在form元素中
### 表单元素
表单元素指的是不同类型的 input 元素、复选框、单选按钮、提交按钮等等
### input元素
`<input>`元素是最重要的表单元素，根据type属性值的不同，input有很多不同的形态
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20190926170223.png)
> 并不止这三种，后面的章节会有更多的介绍
#### 文本输入
`<input type="text">`用于定义文本输入的单行输入字段

```html
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
     <form>
First name:<br>
<input type="text" name="firstname">
<br>
Last name:<br>
<input type="text" name="lastname">
</form>

<p>请注意表单本身是不可见的。</p>

<p>同时请注意文本字段的默认宽度是 20 个字符。</p>   
    </body>
</html>
```
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20190926172720.png)
#### 单选按钮输入
`<input type="radio">` 定义单选按钮。

单选按钮允许用户在有限数量的选项中选择其中之一
#### 提交按钮
`<input type="submit">`定义用于向表单处理程序（form-handler）提交表单的按钮。当`submit`被按下的时候，执行的动作是将所在表单的数据提交到该表单fomr的属性`action`所指向的网址
```html
<!DOCTYPE html>
    <html>
        ...
        <form action="/demo/demo1.asp">
            <input type="submit"/>
        </form>
    </html>
```

属性：
- value：就是submit按钮上所显示的文本
### form表单属性
#### action属性
定义为提交表单时执行的动作，通常是通过提交按钮来执行提交表单，即为执行动作，如果省略action属性，则action会被设置为当前页
#### method属性<sup>?</sup>
规定在提交表单时所用的HTTP方法（GET或者POST）

`<form action="action_page.php" method="GET">`

或者

`<form action="action_page.php" method="POST">`

##### 如何使用GET
GET方法为默认方法，当数据没有敏感信息，比如搜索，而不是提交密码等含有敏感信息时，当使用GET方法时，表单的数据在页面的地址栏是可见的
`action_page.php?firstname=Mickey&lastname=Mouse`

什么时候使用POST
提交敏感信息时，POST的安全性更强，在页面地址栏提交的数据是不可见的
### name属性
如果要被正确的提交，每个输入的字段都必须设置一个name属性，如果不设置name属性，则该输入不会被提交
## fieldset组合表单数据
把表单的数据组合起来，在页面上显示为一个黑色的框框起来为一组，fieldset要写在form里面，也可以写在form外面
### legend元素
legend元素为fieldset元素命名
## form的所有属性
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191001154018.png)
## html所有表单元素
### input
之前已经讲过
### select元素（下拉列表）
option元素来定义带选择的选项，可以通过selected属性来定义与选择的选项
```html
<!DOCTYPE html>
<html>

<head>

</head>

<body>
    <form action="">
        <fieldset>
            <legend>分组名称</legend>
            名字：<input name="name" type="text"/><br/>
            性别：<input name="gender" type="radio" value="男">男<br/>
            爱好：<select name="hobbies" id="">
                <option value="1">篮球</option>
                <option value="2">测试测试测试测试测试</option>
                <option value="3" selected>3</option>
            </select>
        </fieldset>
    </form>
</body>

</html>
```
### textarea元素
该元素定义多行输入字段（文本域）
```html
<textarea name="message" rows="10" cols="30">
The cat was playing in the garden.
</textarea>
```
### buttonn元素
定义可点击按钮
`<button type="button" onclick="alert("hello world")">click me</button>`
## html5表单元素<sup>?</sup>
html5增加了如下表单元素
- datalist
- keygen
- output
### html5表单元素datalist
当用户在输入时会看到预定义的下拉列表，比如用户像输入“百度”，但是只需要输入“百”字，下拉别表中就会出现“百度”的字样
```html
<form action="action_page.php">
<input list="browsers">
<datalist id="browsers">
   <option value="Internet Explorer">
   <option value="Firefox">
   <option value="Chrome">
   <option value="Opera">
   <option value="Safari">
</datalist> 
</form>
``` 
> 与之前的select元素不同的是，datalist使用的时候需要输入一定的信息（当然也可以不输入任何信息像select一样直接下拉列表选择），所以需要提前定义一个输入框`<input list="brosers name="broser"">`,接着在datalist中的id属性中的值为input的list属性的值 
## input元素的输入类型
### 输入类型1：text
`<input type="text" name="address">`
### 输入类型2：password
`<input type="password" name="password">`
### 输入类型3：submit
`<input type="submit" value="提交">`
### 输入类型4：radio
`<input type="radio" name="gender" checked>`

checked:是用来预选定的单选框
### 输入类型5：checkbox
`<input type="checkbox" name="vechile" value="car">car</input>`
### 输入类型6：button
`<input type="button" name="button" onclick="alert("hello world")" value="点击我"/>`
### 输入类型7：html5新增加的输入类型
- color
- date
- datetime
- datatime-local
- email
- month
- number
- range
- serarch
- tel
- time
- url
- week
> 注释：老式web浏览器不支持输入类型时候，会被自动视为text类型
## html input元素的属性
### value属性
该属性规定输入字段的初始值
### readonly属性
`<input type="text" readonly>`
效果是输入框显示在用户面前，但是只是只读，用户不能修改
### disabled属性
`<input type="text" name ="name" disabled>`
disabled 属性规定输入字段是禁用的。

被禁用的元素是不可用和不可点击的。

被禁用的元素不会被提交。
### size属性
输入框显示的长度，size越大，输入框越长（以字符来计算）
### maxlength属性
规定输入字段允许的最大长度（该属性限制用户输入时并不会给用户任何反馈，需要编写javascript来完后）
## html5新增属性
- autocomplete
- autofocus
- form
- formaction
- formmethod
- formenctype
- formnovalidate
- formtarget
- height 和 width
- list
- min 和 max
- multiple
- pattern (regexp)
- placeholder
- required
- step

并为form元素增加了属性
- atuocomplete
- novalldate
