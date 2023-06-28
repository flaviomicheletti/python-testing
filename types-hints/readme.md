# Python types

Python's "typing" module is a powerful feature introduced in Python 3.5 to 
provide optional static type hints and type checking capabilities to the 
language. It allows developers to annotate their code with type hints, which 
provide information about the expected types of variables, function 
arguments, and return values. These type hints serve as documentation and can 
be used by static type checkers and IDEs to detect potential type errors and 
provide better code analysis. 

The motivation behind introducing the "typing" module was to improve code 
maintainability, readability, and to catch type-related errors early in the 
development process. While Python has always been dynamically typed, meaning 
that variables can hold values of any type, the addition of type hints with 
the "typing" module brings a level of static typing to Python, making it 
easier to catch certain classes of bugs and enhance code quality. 

The "typing" module defines a set of classes, functions, and type aliases 
that allow developers to express a wide range of types, including primitive 
types like int, str, bool, etc., as well as more complex types such as 
tuples, lists, dictionaries, and user-defined types. It also supports 
generics, union types, optional types, and more advanced type constructs. 

The type hints provided by the "typing" module are not enforced at runtime by 
default. Python remains dynamically typed, and the type hints are primarily 
used for static type checking. There are external tools like "mypy" that can 
perform static type checking based on the type hints in your code. 

The "typing" module has gained significant popularity and adoption since its 
introduction. It has become an essential part of many Python codebases, 
particularly in larger projects and codebases where type annotations help 
improve collaboration and code maintenance. It has also enabled the 
development of static type checkers like "mypy" and integrated development 
environments (IDEs) that provide more powerful code analysis and 
autocompletion features. 

As of my knowledge cutoff in September 2021, the "typing" module is still 
very much valid and actively maintained in the most current versions of 
Python, including Python 3.9 and later. It has undergone several improvements 
and refinements since its introduction, making it more versatile and capable 
of expressing complex type relationships. However, it's always a good idea to 
refer to the official Python documentation or release notes for the most up-
to-date information on the "typing" module in the current Python version you 
are using.



## More examples

Here's a more comprehensive breakdown: 

Type aliases: The "typing" module allows you to define aliases for complex 
type annotations using the `TypeAlias` function. This can be useful for 
creating shorthand names for frequently used types. 

Type hints for variables: You can annotate variables with type hints using 
the `:` syntax. For example, `x: int = 5` indicates that the variable `x` is 
expected to be of type `int` and is initialized with a value of `5`. 

Type hints for function parameters: Function parameters can be annotated with 
type hints similar to variables. For instance, `def foo(x: int, y: str) -> 
bool:` indicates that `foo` takes an integer `x` and a string `y` as 
parameters. 

Type hints for function return values: The return type of a function can be 
annotated using the `->` syntax. For example, `def bar() -> int:` specifies 
that the `bar` function returns an integer. 

Type hints for collections: The "typing" module provides type hints for 
various collections, such as lists (`List`), tuples (`Tuple`), dictionaries (`
Dict`), sets (`Set`), and more. These type hints allow you to specify the 
expected types of the elements within these collections. 

Generic types: Generics allow you to define types that can work with multiple 
concrete types. The "typing" module provides generic types such as `List[
T]`, `Dict[K, V]`, and `Tuple[T1, T2]`, where `T`, `K`, and `V` represent 
type variables that can be substituted with specific types. 

Union types: Union types allow you to specify that a variable or parameter 
can accept multiple possible types. It is denoted using the `Union` type from 
the "typing" module. For example, `def baz(x: Union[int, str]) -> bool:` 
indicates that `baz` can take either an integer or a string as an argument. 

Optional types: Optional types, represented by the `Optional` type hint, 
allow you to indicate that a variable, function parameter, or return value 
can have the specified type or be `None`. It is equivalent to `Union[type, 
None]`. 

It's worth mentioning that there are more advanced features and constructs 
provided by the "typing" module, such as Callable types, TypeVars, Literal 
types, and more. These additional features enhance the expressiveness and 
flexibility of type hints in Python. 

Keep in mind that the "typing" module has evolved over time, so it's 
advisable to refer to the official Python documentation and release notes for 
the most up-to-date and accurate information on the available features and 
capabilities of the module.


## See Also

- https://realpython.com/python-type-checking/
- http://mypy-lang.org/
- https://betterdatascience.com/python-statically-typed/