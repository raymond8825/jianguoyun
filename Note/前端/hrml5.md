#学习路径
- html
- xhtml
- css
- css3
- javascript
- jquery
- html5
## html5视频标签video
vedio元素目前支持这三种格式的视频

Ogg = 带有 Theora 视频编码和 Vorbis 音频编码的 Ogg 文件

MPEG4 = 带有 H.264 视频编码和 AAC 音频编码的 MPEG 4 文件

WebM = 带有 VP8 视频编码和 Vorbis 音频编码的 WebM 文件
```html
<!DOCTYPE HTML>
<html>
<body>

<video src="/i/movie.ogg"  width="320" height="240" controls="controls">
Your browser does not support the video tag.
</video>

</body>
</html>

```
- control属性：是用来提供控制按钮gui的，否则视频将无法控制播放暂停等功能
- width，height属性：分别来控制视频的长宽
- veido元素的内容：是当浏览器不支持显示该视频的时候，会显示出该内容

当视频要适配到多个浏览器的时候，而某些浏览器支持的视频格式有不一样，所以我们可以准备多个格式的视频，然后供浏览器使用
```html
<video width="320" height="240" controls="controls">
  <source src="movie.ogg" type="video/ogg">
  <source src="movie.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```
video 元素允许多个 source 元素。source 元素可以链接不同的视频文件。浏览器将使用第一个可识别的格式
### video标签的属性
![](https://raw.githubusercontent.com/Raymond0225/picbed/master/img/20191002110132.png)
## html5video+DOM<sup>?</sup>
DOM:Document Object Model，简称DOM
## html5音频audio
该元素使用方法和video元素的方法一摸一样
## html5拖放
拖（drag）放（drop）是h5标准的组成部分，在h5中，拖放是标准的一部分，任何元素都可以拖放
## html5拖放实例<sup>?</sup>
### 设置元素为可拖放
`<img dragable="true" />`
将元素属性dragable设置为true是为了使该元素可拖动
### 拖动的时候触发的事件ondragstart=("方法名(参数)")
### 放到何处去ondragover()
ondragover 事件规定在何处放置被拖动的数据。

默认地，无法将数据/元素放置到其他元素中。如果需要设置允许放置，我们必须阻止对元素的默认处理方式。

这要通过调用 ondragover 事件的 event.preventDefault() 方法（因为该方法默认行为是以链接的形式打开）
### 进行放置ondrop
当放置被拖数据时，会发生 drop 事件。

在上面的例子中，ondrop 属性调用了一个函数，drop(event)：
## html5 Canvas
canvas元素用于在网页上绘制图形
### 什么是Canvas？
HTML5 的 canvas 元素使用 JavaScript 在网页上绘制图像。

画布是一个矩形区域，您可以控制其每一像素。

canvas 拥有多种绘制路径、矩形、圆形、字符以及添加图像的方法
### 创建canvas
`<canvas id="mycanvas" width="200" height="100" ></canvas>`
### 通过javascript来绘制
canvas本身没有绘制能力，所有的绘制工作必须通过javascirpt内部完成
## html5内联svg（可伸缩矢量图形）
```html
<!DOCTYPE html>
<html>
<body>

<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="190">
  <polygon points="100,10 40,180 190,60 10,60 160,180"
  style="fill:lime;stroke:purple;stroke-width:5;fill-rule:evenodd;" />
</svg>

</body>
```
## HTML 5 Canvas vs. SVG<sup>?</sup>
二者都可以创作图形，但是根本上是不一样的
## html5 web存储
### html5在客户端存储数据
存储数据之前都是由cookies来完成的，但是cookies不适合存储大量的数据，因为cookies存储在服务器中，还需要向客户端中传递，效率较低

html5中提供了两种方法来存储数据：
- localStorage - 没有时间限制的数据存储
- sessionStorage - 针对一个 session 的数据存储
### localStorage方法
localStorage 方法存储的数据没有时间限制。第二天、第二周或下一年之后，数据依然可用。
```html
<script type="text/javascript">
localStorage.lastname="Smith";
document.write(localStorage.lastname);
</script>
```
### sessionStorage
sessionStorage 方法针对一个 session(会话) 进行数据存储。当用户关闭浏览器窗口后，数据会被删除。
```html
<script type="text/javascript">
sessionStorage.lastname="Smith";
document.write(sessionStorage.lastname);
</script>
```
# html5高阶属性没有学习