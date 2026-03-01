# GUI编程

图形用户界面（Graphical User Interface，GUI）和工具命令语言（Tool Command Language，TCL）

>  编译Python解释器

客户端/服务端架构：GUI应用程序和窗口系统服务器（网络窗口环境）

GUI编程中的相关概念：

- 顶层窗口
- 控件：父控件、子控件
- 根窗口

> GUI应用的运行由事件驱动处理

Python默认GUI库`tkinter`中的布局管理器：`Placer`、`Packer`和`Grid`

TK控件：

| 控件 | 描述  |
| -----  | -----  |
| Label  | 用于包含文本或图像 | 
| Button | 与Label类似，但提供鼠标悬停、按下和释放等键盘事件 |
| Scale  | 线性滑块控件，根据已设定的起始值和终止值，给出当前设定的精确值 |
| Frame  | 包含其他控件的纯容器 |
| Scrollbar | 为Text、Canvas、Listbox等支持的控件提供滚动功能 |
| Listbox   | 给用户显示一个选项列表进行选择 |
| Entry     | 单行文本框，用于收集键盘输入 |
| Spinbox   | Entry和Button的组合，允许对值进行调整 |
| LabelFrame  | 标签和框架的组合，拥有额外的标签属性  |
| PanedWindow | 一个可以控制其他控件在其中摆放的容器控件 |

> 偏函数

Python流行的GUI工具包：

- Tix（Tk接口扩展）
- Pmw（Python MegaWidgets Tkinter扩展）
- wxPython（wxWidgets的Python版本）
- PyGTK（GTK+的Python版本）

> `.pyw`扩展名阻止DOS命令行或终端窗口弹出




