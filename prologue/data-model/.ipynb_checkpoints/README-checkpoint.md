# Python Data Model

Python's unique features include: tuple unpacking and descriptors

> ⚠️ Immature abstractions are just as harmful as premature optimization

The data model is a description of Python's framework, which standardizes the interfaces of the language's own building blocks, including sequences, iterators, and context managers.

Special methods in classes enable custom objects to implement and support the following language constructs:

- Iteration
- Collections
- Attribute access
- Operator overloading
- Function and method invocation
- Object creation and destruction
- String representation and formatting
- Context management (i.e., `with` blocks)

Iteration is usually implicit. When a collection class doesn't implement the `__contains__` method, the `in` operator performs a sequential iterative search.

> Immutable objects and mutable objects

**CPython Interpreter**

Interactive consoles and debugging programs use the `repr` function to get the string representation of objects. The string returned by `__repr__` should express as much as possible how to create the printed object with code. The `__str__` special method is called when the `str` function or `print` function is used, and returns a user-friendly string for terminal users. When an object doesn't implement the `__str__` function, the interpreter uses `__repr__` as a substitute when obtaining the object's string representation.

> By default, instances of custom classes are always considered true, unless the class implements the `__bool__` or `__len__` function.

[Python Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth)
