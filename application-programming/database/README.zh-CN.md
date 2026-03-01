# 数据库编程

对象关系映射（Object-Relational Mapping， ORM）

> 数据库通常使用文件系统作为底层的持久化存储

数据库的相关概念：数据库模式和游标

在Python中数据库是通过**适配器**访问关系数据库的客户端，且适配器应当符合Python数据库特殊兴趣小组（DB-SIG）的API标准

> DB-API：阐明一些列所需对象和数据库访问机制的标准，为不同数据库适配器和底层数据库系统提供一致性的访问

DB-API标准：

| 属性 | 描述  |
| -----  | -----  |
| apilevel | 兼容的DB-API最高版本，默认值为1.0 |
| threadsafety | 线程安全级别，可选值有0、1、2和3 |
| paramstyle | SQL语句参数风格，参数风格包括`numeric`、`named`、`pyformat`、`qmark`和`format` |
| connect()  | 创建并返回Connection对象访问数据库 |
| Warning    | 警告异常基类 |
| Error      | 错误异常基类 |

**DSN（Data Source Name, 数据源名称）**

Connection对象方法：

| 方法名 | 描述 |
| -----  | -----  |
| close() | 关闭数据库连接 |
| commit() | 提交当前事务 |
| rollback() | 取消当前事务 |
| cursor() | 使用该连接创建并返回一个游标或类似游标的对象 | 
| errorhandler() | 作为给定连接的游标的处理程序 |

> 根据PEP-249，关闭连接而不事先提交变更时，将会导致执行隐式回滚

Cursor对象属性：

| 属性 | 描述 |
| -----  | -----  |
| arraysize | 使用`fetchmany()`方法时，一次取出的结果行数，默认为1 |
| execute() | 执行数据库命令 |
| executemany() | 为给定的所有参数准备并执行数据库命令 |
| fetchone() | 获取查询结果的下一行 |
| fetchmany() | 获取查询结果的下面多行 |
| fetchall()  | 获取查询结果的所有剩余行 |
| callproc()  | 调用存储过程 |
| close()   | 关闭游标 |

类型对象：

| 类型对象 | 描述  |
| -----   | -----  |
| Date | 日期值对象 |
| Time | 时间值对象 |
| Timestamp | 时间戳值对象 |
| Binary | 对应二进制字符串对象 |
| STRING | 基于字符串列的对象 |
| BINARY | 表示长二进制列的对象 |
| NUMBER | 表示数值列的对象 |

NoSQL数据库：

- 文档存储型：MongoDB
- 键-值对型：Redis
- 列存储型：HBase

> MongoDB数据库将数据存储为BSON格式，一种二进制序列化的JSON串

















