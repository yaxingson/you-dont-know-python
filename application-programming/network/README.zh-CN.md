# 网络编程

> IPv6 vs. IPv4

客户端/服务器架构：

- 硬件（专用外围设备）
  - 打印服务器
  - 文件服务器
- 软件
  - web服务器
  - 数据库服务器
  - 窗体服务器

> 进程间通信（Inter Process Communication, IPC）

按照地址家族不同套接字类型：

- 基于文件
  - UNIX套接字（`AF_UNIX`或`AF_LOCAL`）
  - LINUX套接字（`AF_NETLINK`）

- 面向网络
  - 因特网套接字（`AF_INET`或`AF_INET6`）
  - TIPC套接字（`AF_TIPC`）

> 有效的端口号范围为0~65535，其中小于1024的为预留端口号

按照是否连接套接字类型：

- 面向连接

- 无连接


