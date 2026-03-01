-- 数据库管理员授权操作
GRANT ALL PRIVILEGES ON db.table TO 'user'@'hostname' IDENTIFIED BY 'passwd';
GRANT SELECT,INSERT,UPDATE ON db.* TO 'user'@'%' IDENTIFIED BY 'passwd';
FLUSH PRIVILEGES;
