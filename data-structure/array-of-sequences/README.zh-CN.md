# 序列构成的数组

**Unicode字符串**

Python语言中的序列类型：

- 容器序列
  - `list`
  - `tuple`
  - `collections.deque`
- 扁平序列
  - `str`
  - `bytes`
  - `bytearray`
  - `memoryview`
  - `array.array`

序列类型按照能否被修改可分为可变序列（list、bytearray、array.array等）和不可变序列（tuple、str和bytes）


> 👆️ Python会忽略代码里[]、{}和()中的换行，此时可省略书写换行符\

**生成器表达式和迭代器协议**

元组用于没有字段名的记录：

```py
user = ('Glenn Cobb', 'mo@idbakub.jm')
name, email = user

```

> 可迭代元素拆包

*命名切片和多维切片*

[python运行原理可视化](https://www.pythontutor.com)



