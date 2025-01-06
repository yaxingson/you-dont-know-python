# Web客户端和服务器

基本概念:

- WWW(World Wide Web): 分布式超文本系统
- SSL(Secure Socket Layer): 安全套接字层
- URI(Uniform Resource Identifier)：统一资源标识符
- MIME(Multipurpose Internet Mail Extension): 多目标因特网邮件扩展

> 客户端/服务器架构

代理服务器:

- 正向代理
- 反向代理

服务器托管

URL格式:

```txt
prot_sch://user:passwd@host:port/path?query#frag

```

| URL组件  |   描述 |
| -----   | -----  |
| prot_sch |  网络协议或下载方案 |
| user |  用户名或登录 |
| passwd |  用户密码 |
| host |  运行web服务器的主机名 |
| port |  端口号（默认为80） |
| path |  资源文件或CGI应用的路径 |
| query | 连接符&分割的一系列键值对 |
| frag |  指定文档内特定锚 |

