# 参考PyQt5快速开发与实战.pdf
# 代码地址 https://github.com/cxinping/PyQt5
# designer.exe 在目录 D:\orange3\project\biolab\qt5-demo\venv\Lib\site-packages\qt5_applications\Qt\bin

#  pyuic5.exe -o firstmainWin.py .\ui\firstmainWin.ui


# 如何添加的子窗體：直接添加了栅格布局，然后在栅格布局里面添加的子窗体
# 信号和slot都是直接在designer配置的，动作是自己用代码编写的，一般信号和slot是控制鼠标和键盘事件的


objectName，控件对象名称
geometry，相对坐标系。
sizePolicy，控件大小策略。
minimumSize，最小宽度、高度
maximumSize，最大宽度、高度。如果想让窗口或控件的大小固定，则可以将 minimumSize 和 maximumSize 这两个属性设置成一样的数值。
font，字体。
cursor，光标。
windowTitle，窗口标题。
windowsIcon/icon，窗口图标/控件图标。
iconSize，图标大小。
toolTip，提示信息。
statusTip，任务栏提示信息 。
text，控件文本。
shortcut，快捷键。



class TabDemo(QTabWidget):


差不多就这三个吧
5.2的tab
5.4 网页交互
整个第8章节

简单设计下
方案1：修改现有的orange
1 修改app图标及名称
2 直接启动的
3 修改登入后显示的图形界面
    

我先自己做一个
1 创建一个普通部件
2 创建登入界面
3 


self.activate_default_config() 添加了一些默认配置 应该是启动的时候显示的应用名称和版本信息等

直接设置按钮--然后调用js
直接使用tab--然后查看tab是否可以有触发事件