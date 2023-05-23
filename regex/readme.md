# Regex in Python

Here are the definitions of all the functions available in the `re` module in Python:

1. `match(pattern, string, flags=0)`
   - Determine if the regular expression pattern matches at the beginning of the string.

2. `fullmatch(pattern, string, flags=0)`
   - Determine if the regular expression pattern matches the entire string.

3. `search(pattern, string, flags=0)`
   - Scan through the string, looking for any location where the regular expression pattern matches.

4. `findall(pattern, string, flags=0)`
   - Return all non-overlapping matches of the regular expression pattern in the string as a list.

5. `finditer(pattern, string, flags=0)`
   - Return an iterator yielding match objects for all non-overlapping matches of the regular expression pattern in the string.

6. `sub(pattern, repl, string, count=0, flags=0)`
   - Return the string obtained by replacing the leftmost non-overlapping occurrences of the regular expression pattern in the string with the replacement string.

7. `subn(pattern, repl, string, count=0, flags=0)`
   - Perform the same operation as `sub()`, but also return the number of substitutions made.

8. `split(pattern, string, maxsplit=0, flags=0)`
   - Split the string by the occurrences of the regular expression pattern and return a list containing the resulting substrings.

9. `compile(pattern, flags=0)`
   - Compile a regular expression pattern into a regular expression object, which can be used for matching, searching, and other operations.

10. `purge()`
    - Clear the regular expression cache.

11. `template(pattern, flags=0)`
    - Compile a regular expression pattern into a template pattern object, which can be used for efficient multiple substitutions.

12. `escape(string)`
    - Return a string with all non-alphanumeric characters backslashed; this is useful if you want to match an arbitrary literal string.

These are the main functions available in the `re` module for regular expression operations in Python.
