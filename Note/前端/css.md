## css基础语法
### css语法
css规则有两个主要部分构成：选择其和一条或多条声名
`selector {declaration1; declaration2; ... declarationN }`
- 选择器：需要改变样式的html元素
- 声名：有一个属性和属性值组成，二者用冒号分开

`selector{property:value}`

例如：`h1{color:red;font-size:12px}`
功能：将h1元素内的文字颜色定义为红色，同时将字体大小设置为12像素![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191008153227.png)
### css选择器
常用的选择器如下几种：
1. 标签选择器

此种选择器选择影响范围大，尽量应用在层级选择器中。
```html
*{margin:0;padding:0}
div{color:red}   


<div>....</div>   <!-- 对应以上两条样式 -->
<div class="box">....</div>   <!-- 对应以上两条样式 -->
```
2. id选择器

通过id名来选择元素，元素的id名称不能重复，所以一个样式设置项只能对应于页面上一个元素，不能复用，id名一般给程序使用，所以不推荐使用id作为选择器。
```html
#box{color:red} 

<div id="box">....</div>   <!-- 对应以上一条样式，其它元素不允许应用此样式 -->
```
3. 类选择器class

通过类名选择元素，一个类可应用于多个元素，一个元素上也可以使用多个类，应用灵活，可复用，是css中应用最多的一种选择器。
```html
.red{color:red}
.big{font-size:20px}
.mt10{margin-top:10px} 

<div class="red">....</div>
<h1 class="red big mt10">....</h1>
<p class="red mt10">....</p>
```
4. 层级选择器

层级选择器是对类选择器的扩充，当我们想对某个标签下的标签进行设置样式的时候，可以使用层级选择器
```html
.box span{color:red}
.box .red{color:pink}
.red{color:red}

<div class="box">
    <span>....</span>
    <a href="#" class="red">....</a>
</div>

<h3 class="red">....</h3>
```
5.组选择器
多个选择器，如果有同样的样式设置，可以使用组选择器（设置分组的时候，直接使用逗号来分隔）
```html
.box1,.box2,.box3{width:100px;height:100px}
.box1{background:red}
.box2{background:pink}
.box2{background:gold}

<div class="box1">....</div>
<div class="box2">....</div>
<div class="box3">....</div>
```
6. 伪类和伪元素选择器
    
常用的伪类选择器有hover，表示鼠标悬浮在元素上时的状态，伪元素选择器有before和after,它们可以通过样式在元素中插入内容。
```html
.box1:hover{color:red}
.box2:before{content:'行首文字';}
.box3:after{content:'行尾文字';}


<div class="box1">....</div>
<div class="box2">....</div>
<div class="box3">....</div>
```
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191009091423.png)
### 属性值的不同写法
#### 颜色
red还可以写为十六进制的#ff0000:
`p{color:#ff0000;}`
> 不要忘记有分号
 
也可以写成缩写形式
`p{color:#ff00;}`
#### 记得写引号
如果值为若干单词，则给值加引号
`p{font-family:"sans serif";}`
#### 多重声名
为了增加可读性，多个声名要用分号分开的同时，也应该换行增加可读性![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191008153908.png)
## css页面引入方法
1.外联式：通过link标签，链接到外部样式表到页面中。

`<link rel="stylesheet" type="text/css" href="css/main.css">`

2.嵌入式：通过style标签，在网页上创建嵌入的样式表。

`<style type="text/css">
    div{ width:100px; height:100px; color:red }
    ......
</style>`

3.内联式：通过标签的style属性，在标签上直接写样式。

`<div style="width:100px; height:100px; color:red ">......</div>`
## css文本设置
常用的应用文本的css样式：

- color 设置文字的颜色，如： color:red;

- font-size 设置文字的大小，如：font-size:12px;

- font-family 设置文字的字体，如：font-family:'微软雅黑';

- font-style 设置字体是否倾斜，如：font-style:'normal'; 设置不倾斜，font-style:'italic';设置文字倾斜

- font-weight 设置文字是否加粗，如：font-weight:bold; 设置加粗 font-weight:normal 设置不加粗

line-height 设置文字的行高，设置行高相当于在每行文字的上下同时加间距， 如：line-height:24px; ![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191008155356.png)

- font 同时设置文字的几个属性，写的顺序有兼容问题，建议按照如下顺序写： font：是否加粗 字号/行高 字体；如： font:normal 12px/36px '微软雅黑';

- text-decoration 设置文字的下划线，如：text-decoration:none; 将文字下划线去掉

- text-indent 设置文字首行缩进，如：text-indent:24px; 设置文字首行缩进24px 行高
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191008155732.png)
- text-align 设置文字水平对齐方式，如text-align:center 设置文字水平居中
## css盒子模型
> 盒子自己的padding可能会把自己给撑大,但是父级别盒子长宽不受影响，而自己的margin如果超出了父级盒子的范围,则既不会撑大父级也不会压缩自己的范围，而是满足margin-top和margin-left的值，子盒子可能越出父盒子的范围，margin-right和margin-bottom则不再满足
### 盒子模型的解释
就是一个开口的盒子，开口冲向我们，便于我们理解和设置元素![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191009092506.png)
### 设置宽高(width,height，盒子内容的宽高)
```css
width:200px;  /* 设置盒子的宽度，此宽度是指盒子内容的宽度，不是盒子整体宽度(难点) */ 
height:200px; /* 设置盒子的高度，此高度是指盒子内容的高度，不是盒子整体高度(难点) */
```
### 设置边框(border,盒子的边框)
可以设置某一边的边框，如顶部边框
```css
border-top-color:red;/*设置顶部颜色边框为红色*/
boder-top-width:10px;/*设置顶部边框粗细为10px */   
border-top-style:solid;  /* 设置顶部边框的线性为实线，常用的有：solid(实线)  
  dashed(虚线)  dotted(点线); */
```
同时，上面的三句可以简写成一句：
```css
border-top:10px solid red;
```
同理，设置其他的三个边框只需要left，right，bottom，如果四个边框设置都一样，可以合并成一句话：
```css
border:10px solid red;
```
### 设置内间距(padding，盒子与盒子内容的间距)
```css
padding-top：20px;     /* 设置顶部内间距20px */ 
padding-left:30px;     /* 设置左边内间距30px */ 
padding-right:40px;    /* 设置右边内间距40px */ 
padding-bottom:50px;   /* 设置底部内间距50px */
```
padding后面还可以跟3个值，2个值和1个值，它们分别设置的项目如下：
```css
padding：20px 40px 50px; /* 设置顶部内边距为20px，左右内边距为40px，底部内边距为50px */ 
padding：20px 40px; /* 设置上下内边距为20px，左右内边距为40px*/ 
padding：20px; /* 设置四边内边距为20px */
```
### 设置外间距(margin，盒子与盒子之间的间距)
外边距的设置方法和padding的设置方法相同，将上面设置项中的'padding'换成'margin'就是外边距设置方法。
### margin的使用技巧
#### 设置元素水平居中（相对于父级盒子）
margin：xxxpx auto;
#### 设置margin值为负值让元素位移及边框合并
#### 外边距合并
只有垂直的margin相遇时才起作用，水平的margin相遇时为累加的作用，垂直的margin相遇时，只选择较大的margin，小的自动忽略。比如：上面的元素margin-bottom:20px;而下面的元素margin-top:30px;则二者相遇后，间距为30px，而不是20+30=50px;这样做不是bug，二十故意而为之，因为为了使网页布局更美观。![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191010165633.png)
可以看到每一个段落都会有20px的margin，而不是40px。
避免这些现象的三种方法：
1. 合理的使用这种现象(如上所述的布局)
2. 设置margin时，一般设置margin-top
3. 当元素被设置为浮动或者定位时，则不会有这种合并现象
#### margin-top塌陷（bug,且针对margin-top）
两个盒子相互嵌套时出现的bug： 当为里面的盒子设置margin-top时，期望的结果是里面的盒子和外面的盒子的距离，但是此时的margin-top值却传递给外面的盒子，导致外层有了margin-top，而内部的盒子设置的margin-top值没有效果；

解决该bug的三种方法：
1. 外部盒子设置一个边框
2. 外部盒子设置 overflow:hidden
3. 使用伪元素类（最常用）：
```css
.clearfix:before{
    content: '';
    display:table;
}
```
此种方法实际上和第一种方法是差不多的，因为第二种的overflow属性有时候我们需要使用这个属性，当设置为hidden不一定是我们想要的，使用第三种的时候，需要使用`class="box clearfix"`

## css元素溢出
当子元素的尺寸超过父元素的尺寸时，需要设置父元素显示溢出的子元素的方式，设置的方法是通过overflow属性来设置。

overflow的设置项：

1. visible 默认值。内容不会被修剪，会呈现在元素框之外。
2. hidden 内容会被修剪，并且其余内容是不可见的，此属性还有清除浮动.清除margin-top塌陷的功能。
3. scroll 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
4. auto 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
5. inherit 规定应该从父元素继承 overflow 属性的值。

## 1.块元素，内联元素，内敛块元素
HTML 元素指的是从开始标签（start tag）到结束标签（end tag）的所有代码。tag之间的内容叫做元素内容

布局中有三种元素，块元素，内联元素，内联块元素，了解这三种元素的特性，才能熟练度进行页面布局

### 1.1块元素
块元素，也可以称为行元素，布局中常用的标签如：div.p.ul.li.h1~h6.dl.dt.dd等等都是块元素，它在布局中的行为：

- 支持全部的样式
- 如果没有设置宽度，默认的宽度为父级宽度100%
- 盒子占据一行.即使设置了宽度
### 1.2内联元素
内联元素，也可以称为行内元素，布局中常用的标签如：a.span.em.b.strong.i等等都是内联元素，它们在布局中的行为：

- 支持部分样式（不支持宽.高.margin上下.padding上下）
- 宽高由内容决定
- 盒子并在一行
- 代码换行，盒子之间会产生间距
- 子元素是内联元素，父元素可以用text-align属性设置子元素水平对齐方式(这里的text-align属性一旦设置，对其所有子孙级别的元素都成立)
#### 1.2.1 解决内联元素间隙的方法
1. 去点内联元素之间的换行
2. 将内联元素父级设置为font-size为0，内联元素自身设置font-size为0
### 1.3内联块元素
内联块元素也叫行内块元素，是新增的元素类型，但是现有的元素没有归为此类，，img和input元素的行为类似这种元素，但是也归类于内联元素，我们可以用display属性将块元素或者内联元素转化成这种元素。它们在布局中表现的行为：
- 支持全部样式
- 如果没有设置宽高，宽高由内容决定
- 盒子并在一行
- 代码换行，盒子会产生间距
- 子元素是内联块元素，父元素可以用text-align属性设置子元素水平对齐方式。

### 1.4三种元素相互转换
这三种元素，可以通过display属性来相互转化，不过实际开发中，块元素用得比较多，所以我们经常把内联元素转化为块元素，少量转化为内联块，而要使用内联元素时，直接使用内联元素，而不用块元素转化了。
display属性：
- none元素隐藏且不占位置
- block元素以块元素显示
- inline元素以内联元素显示
- inline-block元素以内联块元素显示

 

## 2.浮动
### 2.1浮动特性
1. 浮动元素有左浮动(float:left)和右浮动(float:right)两种

2. 浮动的元素会向左或向右浮动，碰到父元素边界或者其他元素才停下来

3. 相邻浮动的块元素可以并在一行，超出父级宽度就换行

4. 浮动让行内元素或块元素自动转化为行内块元素(此时不会有行内块元素间隙问题，但是如果直接用`display: inline-block`转换为行内块元素的话，虽然像内联元素一样排在一行，但是元素与元素之间会有

5. 浮动元素后面没有浮动的元素会占据浮动元素的位置（排列在浮动元素的整下方），但是当没有浮动的元素内中包含文字的时候，该文字则会避开浮动的元素，形成文字饶图的效果

6. 父元素如果没有设置尺寸(一般是高度不设置)，父元素内整体浮动的元素无法撑开父元素，父元素需要清除浮动

父级元素如何清除浮动呢？
- 父级上增加属性overflow：hidden（后面可能会遇到问题）
- 在最后一个子元素的后面加一个空的div，给它样式属性 clear:both（不推荐，老式做法）
- 使用成熟的清浮动样式类，clearfix（高大上）

```css
.clearfix:after,.clearfix:before{ content: "";display: table;}
.clearfix:after{ clear:both;}/*合并写法，为了解决浮动和margin-top塌陷的问题*/
.clearfix{zoom:1;}/*为了兼容IE浏览器，除此之外，没有意义*/
```

1. 浮动元素之间没有垂直margin的合并

### 2.2父级元素清除浮动<sup>?</sup>
## 3定位<sup>?</sup>
### 3.1文档流
文档流，是指盒子按照html标签编写的顺序依次从上到下，从左到右排列，块元素占一行，行内元素在一行之内从左到右排列，先写的先排列，后写的排在后面，每个盒子都占据自己的位置。<sup>?默认不就是这样的嘛</sup>
### 3.2关于定位
> 一个元素定位后，是浮动起来的，还需要设置对应的偏移值才能进行对对偏移

我们可以使用css的position属性来设置元素的定位类型，postion的设置项如下：

- relative 生成相对定位元素，元素所占据的文档流的位置保留，（因为元素本身所占据文档流位置保留，就意味着该元素之后的元素依然不能向前谋取位置，虽然该元素目前已经浮动起来）元素本身相对自身原位置进行偏移。

- absolute 生成绝对定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于上一个设置了定位的父级元素来进行定位，如果找不到，则相对于body元素进行定位。（加入该元素父级为div，如果div中没有设置position属性，则会以body为基准定位，如果div中设置了position属性I，属性值一般为relative，则该元素以div为基准定位偏移,与此同时，该元素下面的元素会因为该元素的绝对定位偏移而占据该元素的位置，因为该元素是“绝对定位”不是“相对定位”）

- fixed 生成固定定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于浏览器窗口进行定位。

- static 默认值，没有定位，元素出现在正常的文档流中，相当于取消定位属性或者不设置定位属性。

- inherit 从父元素继承 position 属性的值。

### 3.3定位元素的偏移
定位的元素还需要使用left，right，top，bottom来设置相对于参照元素的偏移值
### 3.4定位元素的层级
定位元素是浮动的正常的文档流之上的，可以用z-index属性来设置元素的层级
### 3.5定位元素特性 
绝对定位和固定定位的块元素和行内元素会自动转化为行内块元素
## 4. background属性
### 4.1. 属性解释
background属性是css中应用比较多，且比较重要的一个属性，它是负责给盒子设置背景图片和背景颜色的，background是一个复合属性，它可以分解成如下几个设置项：
- background-color 设置背景颜色
- background-image 设置背景图片地址
- background-repeat 设置背景图片如何重复平铺
- background-position 设置背景图片的位置
- background-attachment 设置背景图片是固定还是随着页面滚动条滚动

实际应用中，我们可以用background属性将上面所有的设置项放在一起，而且也建议这么做，这样做性能更高，而且兼容性更好，比如：“background: #00FF00 url(bgimage.gif) no-repeat left center fixed”，这里面的“#00ff00”是设置background-color；“url(bgimage.gif)”是设置background-image；“no-repeat”是设置background-repeat；“left center”是设置background-position；“fixed”是设置background-attachment，各个设置项用空格隔开，有的设置项不写也是可以的，它会使用默认值。
## 5 实例编写
### 5.1 翻页样式
首先大会于这种，我们可以使用无序列表标签`ul`,由于有页面十个链接，我们使用快捷方式创建十个链接`ul.pagenation>(li>a{1})*10`，然后点击tab键就会自动生成十个`a`标签
```html
<ul class="pagenation">
    <li><a href="">1</a></li>
    <li><a href="">1</a></li>
    <li><a href="">1</a></li>
    <li><a href="">1</a></li>
    <li><a href="">1</a></li>
    <li><a href="">1</a></li>
    <li><a href="">1</a></li>
    <li><a href="">1</a></li>
    <li><a href="">1</a></li>
    <li><a href="">1</a></li>
</ul>
```
由于使用`ul`来作为标签，`ul`默认带有自己的margin,padding同时在浏览器上`li`标签还带有一个点，但是这个点往往在不同的浏览器上兼容性不好，我们应该放弃使用这个点，这个在浏览器中的检查选项中可以看到`ul`标签这两个属性的大小值，我们需要将其清空,我们在css文件中写入
```css
    .pagenation{
        list-style: none;
        margin: 10px auto 0px;
        padding:0;
    }
```
此时，这些页码排列顺序是竖直排列的，不是横着排列，因为`li`元素是块元素，会自动换到下一行，所以我们使用display属性来将块元素转为内联块元素（inline-block，这样虽然是内联块元素，但是仍然能设置宽高，所以内联块元素和块元素用的最多）
```css
    .pagenation li{
        display: inline-block;
    }
```
这样就可以将竖直排列的页码转换为横着排列，但是这些页码之间有空格，在浏览器上检查发现margin值为0，不应该有空格，此时解决方法是：
第一种方法：将内联元素的html代码中的换行删除，这样就可以消除元素之间的莫名其妙的空格
第二种方法：将内联元素的父级设置font-size为0，内联元素自身再设置font-size

我们采用第二种方法，当我们将所有的页码之间的空格删除之后，我们开始布置自己的格式，首先将所有的页码显示的页面中间，因为所有的页面都是内联块元素，可以将父元素的`text-align`属性设置为`center`。居中之后，我们将字体设置为12px,高度为26px,margin为8px 5px 8px;然后设置padding为0px 10px 0px来使得页码和背景色相适应。当要调节文字和背景的相对位置的时候，使用`line-height`来设置，使用`height`是不行的，因为`a`标签是内联元素标签，不支持设置宽高。

