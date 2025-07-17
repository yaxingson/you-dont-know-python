# Python Data Model

> ⚠️ Immature abstractions can be just as harmful as premature optimization.

Core architecture of the Python language:

- Iteration
- Collection types
- Attribute access
- Operator overloading
- Function and method calls
- Object creation and destruction
- String representation and formatting
- Context management (i.e., the `with` block)

**Mutable and Immutable Objects**

> String representation of objects: The interactive console and debuggers use the `repr` function to obtain a string representation of an object, aiming to show how the object could be recreated in code; the `print` function uses the `str` function to get a user-friendly string representation for terminal output. If an object does not implement the `__str__` method and the Python interpreter needs to call it, the interpreter will use `__repr__` as a fallback.

By default, instances of custom classes are always considered true in a boolean context, unless the class defines the special methods `__bool__` or `__len__`.
