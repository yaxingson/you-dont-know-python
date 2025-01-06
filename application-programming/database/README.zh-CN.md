# 数据库编程

相关概念:

- ORM(Object Relational Mapping): 对象关系映射
- RDBMS(Relational Database Management System): 关系数据库管理系统

持久化存储方案:

- 文件系统
- 数据库系统

> 游标

```sql
- 创建数据库

CREATE DATABASE test;
GRANT ALL ON test.* to user;

- 使用数据库

USE test;

- 删除数据库

DROP DATABASE test;

- 创建表

CREATE TABLE users (
  username VARCHAR(8),
  user_id INT,
  proj_id INT
);

- 删除表

DROP TABLE users;

- 插入行

INSERT INTO users VALUES('leanna', 2102, 1);

- 更新行

UPDATE users SET proj_id=4 WHERE user_id=2102;

- 删除行

DELETE FROM users WHERE proj_id=1;

```

