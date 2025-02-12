clasname - pascal
var - snake case

credit-deposit , transctiosn in csv
```
1. Code Layout
Indentation: Use 4 spaces per indentation level (no tabs).
Maximum Line Length: Keep lines ≤79 characters (72 for docstrings/comments).
Blank Lines:
Use two blank lines before top-level functions and classes.
Use one blank line inside functions to separate logic.
Imports:
Each import should be on a new line.
Order: standard library → third-party modules → local imports.
Use absolute imports over relative imports.

2. Naming Conventions
Variables & Functions: snake_case (e.g., my_variable, calculate_sum()).
Classes: PascalCase (e.g., MyClass).
Constants: UPPER_CASE_WITH_UNDERSCORES.
Private members: Prefix with _ (e.g., _internal_var)

3. Whitespace Usage
No spaces inside parentheses, brackets, or braces: func(arg1, arg2), not func( arg1, arg2 ).
One space around operators: x = a + b, not x=a+b.
No extra spaces in function calls: func(1, 2), not func( 1, 2 ).

4. String Formatting
Prefer f-strings (f"Hello {name}") over % formatting or .format().

5. Comments & Docstrings
Use inline comments sparingly and write complete sentences (# Explain why, not what).
Use docstrings ("""Triple quotes""") for modules, functions, and classes

6. Miscellaneous
Use is for comparisons with None: if value is None:, not if value == None:.
Avoid from module import *.
Use with for resource management (e.g., with open("file.txt") as f:).
```

### packages that automatically format Python code
```
Black: Best if you want a strict and consistent formatter with zero configuration.
autopep8: If you want a lighter, more flexible PEP 8 fixer.

pylint (For Naming Convention Warnings) : gives score

- To fix trailing whitespace, indentation, and long lines, run:
autopep8 --in-place --aggressive --aggressive "bank copy 2.py"

- Fix Naming Conventions
Pylint flagged functions like:
ruff check --fix "bank copy 2.py"

```