# 网络编程

> 事务

客户端/服务端架构：

1. 硬件系统：打印服务器（打印机）和文件服务器（磁盘驱动器）
2. 软件系统：Web服务器、数据库服务器和窗体服务器

> 网络化窗体环境

**进程间通信（IPC）**

套接字类型：

1. 基于文件：AF_UNIX/AF_LOCAL
2. 面向网络：AF_INET/AF_INET6

有效端口号范围为0~65535，小于1024的端口号为系统预留端口号

套接字连接风格：

1. 面向连接：TCP套接字（SOCK_STREAM）
2. 无连接：UDP套接字（SOCK_DGRAM）

> 伪代码

阻塞套接字和非阻塞套接字

优雅地退出和调用服务器:

```python
import socket

socket = socket.socket()

socket.close()

```

> 同步与异步服务器











