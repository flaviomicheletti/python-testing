# dictionary unpacking

"Dictionary unpacking" is a feature in Python that allows you to merge or 
combine dictionaries using the double asterisks (**). It provides a concise 
way to merge dictionaries or add new key-value pairs to an existing 
dictionary. 

The syntax for dictionary unpacking is as follows:

```python
new_dict = {**dict1, **dict2, **dict3}
```

Here, `dict1`, `dict2`, and `dict3` are dictionaries that you want to merge. 
The double asterisks (**), when used with dictionaries, unpacks the key-value 
pairs from each dictionary and merges them into a new dictionary. 

When merging dictionaries, if there are duplicate keys, the value from the 
rightmost dictionary takes precedence. This means that if a key is present in 
multiple dictionaries being merged, the value associated with that key in the 
rightmost dictionary will overwrite the previous values. 

In addition to merging dictionaries, you can also use dictionary unpacking to 
add new key-value pairs to an existing dictionary. Here's an example: 

```python
original_dict = {"a": 1, "b": 2}

extended_dict = {**original_dict, "c": 3, "d": 4}
```

In this example, the dictionary unpacking operator (**), along with the 
additional key-value pairs, adds new entries "c": 3 and "d": 4 to the `
original_dict`, creating a new dictionary `extended_dict`. 

Dictionary unpacking can be especially useful when working with configuration 
files, merging default configurations with user-defined configurations, or 
when passing a dictionary as keyword arguments to a function. 

It's important to note that dictionary unpacking is available in Python 3.5 
and later versions. 


